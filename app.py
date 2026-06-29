# app.py
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Progress, RoadmapHistory
from planner import get_roadmap
import json, os

# ── Load .env file automatically ──
from dotenv import load_dotenv
load_dotenv()   # reads SECRET_KEY and GROQ_API_KEY from your .env file

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-key-change-in-production")

# ── Database — PostgreSQL on Render, SQLite locally ──
DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///database.db")
# Render gives postgres:// but SQLAlchemy needs postgresql://
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message = "Please log in to access this page."

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))


# ── DB init ─────────────────────────────────
with app.app_context():
    db.create_all()


# ── HOME ────────────────────────────────────
@app.route("/")
def index():
    return render_template("index.html")


# ── SIGNUP ──────────────────────────────────
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        email    = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        confirm  = request.form.get("confirm_password", "")

        if not username or not email or not password:
            flash("All fields are required.", "error")
            return render_template("signup.html")
        if password != confirm:
            flash("Passwords do not match.", "error")
            return render_template("signup.html")
        if User.query.filter_by(email=email).first():
            flash("Email already registered.", "error")
            return render_template("signup.html")
        if User.query.filter_by(username=username).first():
            flash("Username already taken.", "error")
            return render_template("signup.html")

        user = User(
            username=username,
            email=email,
            password=generate_password_hash(password)
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)
        flash("Account created! Welcome to PathForge.", "success")
        return redirect(url_for("dashboard"))

    return render_template("signup.html")


# ── LOGIN ───────────────────────────────────
@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))
    if request.method == "POST":
        email    = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user, remember=True)
            flash(f"Welcome back, {user.username}!", "success")
            return redirect(url_for("dashboard"))
        flash("Invalid email or password.", "error")
    return render_template("login.html")


# ── LOGOUT ──────────────────────────────────
@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for("index"))


# ── DASHBOARD ───────────────────────────────
@app.route("/dashboard")
@login_required
def dashboard():
    history = RoadmapHistory.query.filter_by(user_id=current_user.id)\
                .order_by(RoadmapHistory.created_at.desc()).all()

    # Stats
    total_roadmaps = len(history)
    active_roadmap = next((h for h in history if h.status == "active"), None)

    # Overall skill stats across all roadmaps
    all_progress = Progress.query.filter_by(user_id=current_user.id).all()
    total_skills     = len(all_progress)
    completed_skills = sum(1 for p in all_progress if p.completed)
    overall_pct      = round((completed_skills / total_skills * 100) if total_skills else 0)

    return render_template(
        "dashboard.html",
        history=history,
        active_roadmap=active_roadmap,
        total_roadmaps=total_roadmaps,
        total_skills=total_skills,
        completed_skills=completed_skills,
        overall_pct=overall_pct,
    )


# ── GENERATE FORM ───────────────────────────
@app.route("/generate", methods=["GET"])
@login_required
def generate():
    return render_template("generate.html")


# ── GENERATE POST ───────────────────────────
@app.route("/generate", methods=["POST"])
@login_required
def generate_post():
    goal         = request.form.get("goal", "").strip()
    level        = request.form.get("level", "beginner")
    duration     = int(request.form.get("duration", 3))
    hours_per_day = int(request.form.get("hours_per_day", 2))

    if not goal:
        flash("Please enter a career goal.", "error")
        return redirect(url_for("generate"))

    roadmap = get_roadmap(goal, level, duration, hours_per_day)

    if roadmap.get("source") == "ai_error":
        error_msg = roadmap.get("error", "Unknown error")
        # Common helpful hints
        if "GROQ_API_KEY" in error_msg:
            flash("Groq API key missing. Add GROQ_API_KEY=gsk_xxx to your .env file and restart the app.", "error")
        elif "invalid JSON" in error_msg:
            flash("AI returned an invalid response. Please try again — it usually works on retry.", "error")
        else:
            flash(f"AI generation failed: {error_msg}", "error")
        return redirect(url_for("generate"))

    # Save roadmap to history
    history_entry = RoadmapHistory(
        user_id=current_user.id,
        goal=roadmap["goal"],
        level=roadmap["level"],
        duration=roadmap["duration"],
        hours_per_day=roadmap["hours_per_day"],
        source=roadmap["source"],
        roadmap_json=json.dumps(roadmap),
        status="active"
    )
    # Set any previous active roadmaps to paused
    RoadmapHistory.query.filter_by(user_id=current_user.id, status="active")\
        .update({"status": "paused"})

    db.session.add(history_entry)
    db.session.commit()

    # Pre-populate progress rows (unchecked)
    for skill in roadmap.get("skills", []):
        existing = Progress.query.filter_by(
            user_id=current_user.id,
            roadmap_id=history_entry.id,
            skill_name=skill["name"]
        ).first()
        if not existing:
            db.session.add(Progress(
                user_id=current_user.id,
                roadmap_id=history_entry.id,
                skill_name=skill["name"],
                completed=False
            ))
    db.session.commit()

    session["current_roadmap_id"] = history_entry.id

    # ── Send email with PDF in background ──
    try:
        from mailer import send_roadmap_email
        from ai_generator import generate_pdf_bytes
        pdf_bytes = generate_pdf_bytes(roadmap)
        result = send_roadmap_email(
            to_email  = current_user.email,
            username  = current_user.username,
            roadmap   = roadmap,
            pdf_bytes = pdf_bytes,
        )
        if result["success"]:
            flash(f"✅ Roadmap emailed to {current_user.email} with PDF attached!", "success")
        else:
            print(f"[Email warning]: {result['error']}")
            # Don't block the user — email is optional
    except Exception as e:
        print(f"[Email error]: {e}")

    return redirect(url_for("roadmap", roadmap_id=history_entry.id))


# ── ROADMAP VIEW ────────────────────────────
@app.route("/roadmap/<int:roadmap_id>")
@login_required
def roadmap(roadmap_id):
    entry = RoadmapHistory.query.filter_by(
        id=roadmap_id, user_id=current_user.id
    ).first_or_404()

    roadmap_data = json.loads(entry.roadmap_json)

    # Load progress for this roadmap
    progress_rows = Progress.query.filter_by(
        user_id=current_user.id,
        roadmap_id=roadmap_id
    ).all()
    progress_map = {p.skill_name: p.completed for p in progress_rows}

    total     = len(progress_map)
    completed = sum(1 for v in progress_map.values() if v)
    pct       = round((completed / total * 100) if total else 0)

    return render_template(
        "roadmap.html",
        roadmap=roadmap_data,
        progress_map=progress_map,
        completed=completed,
        total=total,
        pct=pct,
        roadmap_id=roadmap_id,
        entry=entry,
    )


# ── HISTORY ─────────────────────────────────
@app.route("/history")
@login_required
def history():
    entries = RoadmapHistory.query.filter_by(user_id=current_user.id)\
                .order_by(RoadmapHistory.created_at.desc()).all()
    enriched = []
    for e in entries:
        prog = Progress.query.filter_by(user_id=current_user.id, roadmap_id=e.id).all()
        total = len(prog)
        done  = sum(1 for p in prog if p.completed)
        pct   = round((done / total * 100) if total else 0)
        enriched.append({"entry": e, "pct": pct, "done": done, "total": total})
    return render_template("history.html", entries=enriched)


# ── SAVE PROGRESS (AJAX) ────────────────────
@app.route("/save_progress", methods=["POST"])
@login_required
def save_progress():
    data       = request.get_json()
    skill_name = data.get("skill_name")
    roadmap_id = data.get("roadmap_id")
    completed  = data.get("completed", False)

    row = Progress.query.filter_by(
        user_id=current_user.id,
        roadmap_id=roadmap_id,
        skill_name=skill_name
    ).first()

    if row:
        row.completed = completed
    else:
        db.session.add(Progress(
            user_id=current_user.id,
            roadmap_id=roadmap_id,
            skill_name=skill_name,
            completed=completed
        ))
    db.session.commit()

    # Recalculate overall %
    all_prog  = Progress.query.filter_by(user_id=current_user.id, roadmap_id=roadmap_id).all()
    total     = len(all_prog)
    done      = sum(1 for p in all_prog if p.completed)
    pct       = round((done / total * 100) if total else 0)

    # Mark roadmap complete in history
    if pct == 100:
        entry = db.session.get(RoadmapHistory, roadmap_id)
        if entry:
            entry.status = "completed"
            db.session.commit()

    return jsonify({"success": True, "pct": pct, "done": done, "total": total})


# ── DELETE ROADMAP ───────────────────────────
@app.route("/delete_roadmap/<int:roadmap_id>", methods=["POST"])
@login_required
def delete_roadmap(roadmap_id):
    entry = RoadmapHistory.query.filter_by(
        id=roadmap_id, user_id=current_user.id
    ).first_or_404()
    Progress.query.filter_by(roadmap_id=roadmap_id).delete()
    db.session.delete(entry)
    db.session.commit()
    flash("Roadmap deleted.", "info")
    return redirect(url_for("history"))


# ── AI CHAT — GENERAL ───────────────────────
@app.route("/chat")
@login_required
def chat_page():
    return render_template("chat.html")


@app.route("/chat/general", methods=["POST"])
@login_required
def chat_general():
    from chat import general_chat
    data    = request.get_json()
    message = data.get("message", "").strip()
    history = data.get("history", [])
    if not message:
        return jsonify({"success": False, "error": "Empty message"})
    try:
        response = general_chat(message, history)
        return jsonify({"success": True, "response": response})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})


@app.route("/chat/roadmap", methods=["POST"])
@login_required
def chat_roadmap():
    from chat import roadmap_chat
    data       = request.get_json()
    message    = data.get("message", "").strip()
    roadmap_id = data.get("roadmap_id")
    history    = data.get("history", [])

    if not message:
        return jsonify({"success": False, "error": "Empty message"})

    entry = RoadmapHistory.query.filter_by(
        id=roadmap_id, user_id=current_user.id
    ).first()
    if not entry:
        return jsonify({"success": False, "error": "Roadmap not found"})

    roadmap_data = json.loads(entry.roadmap_json)
    progress_rows = Progress.query.filter_by(
        user_id=current_user.id, roadmap_id=roadmap_id
    ).all()
    progress_map = {p.skill_name: p.completed for p in progress_rows}

    try:
        response = roadmap_chat(message, roadmap_data, progress_map, history)
        return jsonify({"success": True, "response": response})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})


# ── RESEND EMAIL ────────────────────────────
@app.route("/send_email/<int:roadmap_id>")
@login_required
def send_email(roadmap_id):
    entry = RoadmapHistory.query.filter_by(
        id=roadmap_id, user_id=current_user.id
    ).first_or_404()
    roadmap_data = json.loads(entry.roadmap_json)
    try:
        from mailer import send_roadmap_email
        from ai_generator import generate_pdf_bytes
        pdf_bytes = generate_pdf_bytes(roadmap_data)
        result = send_roadmap_email(
            to_email  = current_user.email,
            username  = current_user.username,
            roadmap   = roadmap_data,
            pdf_bytes = pdf_bytes,
        )
        if result["success"]:
            flash(f"📧 Roadmap PDF sent to {current_user.email}!", "success")
        else:
            flash(f"Email failed: {result['error']}", "error")
    except Exception as e:
        flash(f"Email error: {e}", "error")
    return redirect(url_for("roadmap", roadmap_id=roadmap_id))


# ── ADMIN: CACHE VIEWER ─────────────────────
@app.route("/admin/cache")
@login_required
def admin_cache():
    from models import CachedRoadmap
    entries = CachedRoadmap.query.order_by(CachedRoadmap.hit_count.desc()).all()

    enriched = []
    for c in entries:
        data = json.loads(c.roadmap_json)
        enriched.append({
            "id":          c.id,
            "goal":        c.goal,
            "level":       c.level,
            "hit_count":   c.hit_count,
            "skill_count": len(data.get("skills", [])),
            "created_at":  c.created_at,
            "last_used_at":c.last_used_at,
        })

    total_hits     = sum(c.hit_count for c in entries)
    ai_calls_saved = sum(c.hit_count - 1 for c in entries)
    unique_careers = len(set(c.goal.lower() for c in entries))

    return render_template(
        "admin.html",
        cached_roadmaps=enriched,
        total_cached=len(entries),
        total_hits=total_hits,
        ai_calls_saved=ai_calls_saved,
        unique_careers=unique_careers,
    )


@app.route("/admin/cache/preview/<int:cache_id>")
@login_required
def admin_cache_preview(cache_id):
    from models import CachedRoadmap
    entry = db.session.get(CachedRoadmap, cache_id)
    if not entry:
        flash("Cached roadmap not found.", "error")
        return redirect(url_for("admin_cache"))
    roadmap = json.loads(entry.roadmap_json)
    return render_template(
        "admin_preview.html",
        roadmap=roadmap,
        hit_count=entry.hit_count,
        cached_on=entry.created_at.strftime("%d %b %Y"),
    )


@app.route("/admin/cache/delete/<int:cache_id>", methods=["POST"])
@login_required
def admin_cache_delete(cache_id):
    from models import CachedRoadmap
    entry = db.session.get(CachedRoadmap, cache_id)
    if entry:
        db.session.delete(entry)
        db.session.commit()
        flash(f"Deleted cached roadmap: {entry.goal} ({entry.level})", "info")
    return redirect(url_for("admin_cache"))


# ── PDF EXPORT ──────────────────────────────
@app.route("/download_pdf/<int:roadmap_id>")
@login_required
def download_pdf(roadmap_id):
    from ai_generator import generate_pdf
    entry = RoadmapHistory.query.filter_by(
        id=roadmap_id, user_id=current_user.id
    ).first_or_404()
    roadmap_data = json.loads(entry.roadmap_json)
    return generate_pdf(roadmap_data)


if __name__ == "__main__":
    app.run(debug=True)