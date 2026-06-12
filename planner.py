# planner.py
# ─────────────────────────────────────────────────────────────
#  Decision flow:
#
#  User enters goal
#       │
#       ▼
#  Match manual roadmaps?  ──YES──▶  Return instantly (offline)
#       │
#      NO
#       │
#       ▼
#  Found in AI cache DB?   ──YES──▶  Return from DB (no API call)
#       │                              + increment hit_count
#      NO
#       │
#       ▼
#  Call Groq AI API
#       │
#       ▼
#  Save to cache DB forever
#       │
#       ▼
#  Return to user
# ─────────────────────────────────────────────────────────────

import json
import os
import re
from datetime import datetime
from dotenv import load_dotenv
from roadmaps import ROADMAP_REGISTRY

load_dotenv()


# ─────────────────────────────────────────────
#  HELPERS
# ─────────────────────────────────────────────
def _normalize(text: str) -> str:
    return text.lower().strip()


def _make_cache_key(goal: str, level: str) -> str:
    """Unique key per career+level combination."""
    return f"{_normalize(goal)}|{_normalize(level)}"


# ─────────────────────────────────────────────
#  MANUAL MATCHER
# ─────────────────────────────────────────────
def _find_manual_key(goal: str):
    norm = _normalize(goal)
    for key in ROADMAP_REGISTRY:
        if key == norm:        return key
        if key in norm:        return key
        if norm in key:        return key
    return None


def _load_manual(key: str, level: str, duration: int, hours: int) -> dict:
    level_key = _normalize(level)
    if level_key not in ("beginner", "intermediate", "advanced"):
        level_key = "beginner"
    roadmap = dict(ROADMAP_REGISTRY[key][level_key])
    roadmap["duration"]      = f"{duration} months"
    roadmap["hours_per_day"] = hours
    roadmap["source"]        = "manual"
    return roadmap


# ─────────────────────────────────────────────
#  CACHE — read & write  (uses Flask app context)
# ─────────────────────────────────────────────
def _get_from_cache(goal: str, level: str, duration: int, hours: int):
    """
    Look up the DB cache. Returns a roadmap dict if found, else None.
    Also updates hit_count and last_used_at.
    """
    try:
        from models import db, CachedRoadmap
        key = _make_cache_key(goal, level)
        cached = CachedRoadmap.query.filter_by(cache_key=key).first()
        if cached:
            roadmap = json.loads(cached.roadmap_json)
            # Patch with user's chosen duration & hours (cache stores template)
            roadmap["duration"]      = f"{duration} months"
            roadmap["hours_per_day"] = hours
            roadmap["source"]        = "ai_cached"
            # Update stats
            cached.hit_count   += 1
            cached.last_used_at = datetime.utcnow()
            db.session.commit()
            print(f"[Cache HIT] '{goal}' level='{level}' (used {cached.hit_count} times)")
            return roadmap
    except Exception as e:
        print(f"[Cache read error]: {e}")
    return None


def _save_to_cache(goal: str, level: str, roadmap: dict):
    """
    Save an AI-generated roadmap to the DB cache permanently.
    Silently skips if already exists (race condition safety).
    """
    try:
        from models import db, CachedRoadmap
        key = _make_cache_key(goal, level)
        exists = CachedRoadmap.query.filter_by(cache_key=key).first()
        if exists:
            return  # already cached, skip
        entry = CachedRoadmap(
            cache_key    = key,
            goal         = roadmap.get("goal", goal),
            level        = level,
            roadmap_json = json.dumps(roadmap),
            hit_count    = 1,
        )
        db.session.add(entry)
        db.session.commit()
        print(f"[Cache SAVED] '{goal}' level='{level}' → stored in DB for future use")
    except Exception as e:
        print(f"[Cache save error]: {e}")


# ─────────────────────────────────────────────
#  JSON CLEANER
# ─────────────────────────────────────────────
def _clean_json(raw: str) -> str:
    raw = raw.strip()
    raw = re.sub(r'^```(?:json)?\s*', '', raw)
    raw = re.sub(r'\s*```$', '', raw)
    raw = raw.strip()
    match = re.search(r'\{.*\}', raw, re.DOTALL)
    if match:
        return match.group(0)
    return raw


# ─────────────────────────────────────────────
#  GROQ AI GENERATOR
# ─────────────────────────────────────────────
_SYSTEM_PROMPT = """
You are a career roadmap generator. You MUST return ONLY a valid JSON object.
No explanation. No markdown. No text before or after. Just the raw JSON.

The JSON structure must be exactly:
{
  "goal": "Career Goal Name",
  "level": "Beginner",
  "duration": "3 months",
  "hours_per_day": 2,
  "source": "ai",
  "skills": [
    {
      "name": "Skill Name",
      "duration": "2 weeks",
      "topics": ["topic1", "topic2", "topic3"],
      "tasks": ["task1", "task2"],
      "resources": [
        {"title": "Resource Name", "url": "https://example.com"}
      ]
    }
  ]
}

Rules:
- Include exactly 5 to 7 skills.
- Each skill: 3 to 5 topics, 1 to 2 tasks, 1 to 2 resources with real URLs.
- All resource URLs must be real, free, publicly accessible websites.
- Spread skill durations to match the overall duration.
- Output ONLY the JSON. Nothing else.
""".strip()


def _generate_with_groq(goal: str, level: str, duration: int, hours: int) -> dict:
    api_key = os.environ.get("GROQ_API_KEY", "").strip()
    if not api_key:
        raise ValueError("GROQ_API_KEY missing in .env file.")

    try:
        from groq import Groq
    except ImportError:
        raise ImportError("Run: pip install groq")

    client = Groq(api_key=api_key)

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": _SYSTEM_PROMPT},
            {"role": "user",   "content": (
                f"Generate a career roadmap for:\n"
                f"Career Goal: {goal}\n"
                f"Level: {level}\n"
                f"Duration: {duration} months\n"
                f"Daily Study Hours: {hours} hours per day\n\n"
                f"Return ONLY the JSON object. No other text."
            )},
        ],
        temperature=0.3,
        max_tokens=3000,
    )

    raw = response.choices[0].message.content
    print(f"[Groq] Generated roadmap for '{goal}' ({level})")

    cleaned = _clean_json(raw)
    try:
        roadmap = json.loads(cleaned)
    except json.JSONDecodeError as e:
        raise ValueError(f"AI returned invalid JSON: {e}")

    roadmap["goal"]          = roadmap.get("goal", goal)
    roadmap["level"]         = roadmap.get("level", level)
    roadmap["duration"]      = roadmap.get("duration", f"{duration} months")
    roadmap["hours_per_day"] = roadmap.get("hours_per_day", hours)
    roadmap["source"]        = "ai"
    roadmap["skills"]        = roadmap.get("skills", [])
    return roadmap


# ─────────────────────────────────────────────
#  PUBLIC API — called from app.py
# ─────────────────────────────────────────────
def get_roadmap(goal: str, level: str, duration: int, hours: int) -> dict:
    """
    Priority order:
      1. Manual curated roadmaps  (instant, offline)
      2. DB cache                 (instant, no API call)
      3. Groq AI generation       (API call, then saved to cache)
    """

    # ── 1. Manual match ──
    key = _find_manual_key(goal)
    if key:
        print(f"[Planner] MANUAL match: '{key}' for '{goal}'")
        return _load_manual(key, level, duration, hours)

    # ── 2. Cache hit ──
    cached = _get_from_cache(goal, level, duration, hours)
    if cached:
        return cached

    # ── 3. Groq AI call ──
    print(f"[Planner] CACHE MISS → calling Groq AI for '{goal}' ({level})")
    try:
        roadmap = _generate_with_groq(goal, level, duration, hours)
        # Save to cache so next student gets it instantly
        _save_to_cache(goal, level, roadmap)
        return roadmap
    except Exception as e:
        print(f"[Planner ERROR]: {e}")
        return {
            "goal":          goal,
            "level":         level,
            "duration":      f"{duration} months",
            "hours_per_day": hours,
            "source":        "ai_error",
            "error":         str(e),
            "skills":        [],
        }


# ─────────────────────────────────────────────
#  ADMIN HELPERS (optional — use in Flask shell)
# ─────────────────────────────────────────────
def list_cached_roadmaps():
    """Print all cached roadmaps. Run in Flask shell: from planner import list_cached_roadmaps; list_cached_roadmaps()"""
    from models import CachedRoadmap
    all_cached = CachedRoadmap.query.order_by(CachedRoadmap.hit_count.desc()).all()
    print(f"\n{'GOAL':<30} {'LEVEL':<15} {'HITS':<8} CACHED ON")
    print("-" * 70)
    for c in all_cached:
        print(f"{c.goal:<30} {c.level:<15} {c.hit_count:<8} {c.created_at.strftime('%d %b %Y')}")
    print(f"\nTotal cached: {len(all_cached)}")