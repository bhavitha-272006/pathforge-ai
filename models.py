# models.py
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id         = db.Column(db.Integer, primary_key=True)
    username   = db.Column(db.String(80),  unique=True, nullable=False)
    email      = db.Column(db.String(120), unique=True, nullable=False)
    password   = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    progress  = db.relationship("Progress",       backref="user", lazy=True, cascade="all, delete-orphan")
    roadmaps  = db.relationship("RoadmapHistory", backref="user", lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f"<User {self.username}>"


class RoadmapHistory(db.Model):
    __tablename__ = "roadmap_history"
    id            = db.Column(db.Integer, primary_key=True)
    user_id       = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    goal          = db.Column(db.String(200), nullable=False)
    level         = db.Column(db.String(50),  nullable=False)
    duration      = db.Column(db.String(50),  nullable=False)
    hours_per_day = db.Column(db.Integer,     nullable=False, default=2)
    source        = db.Column(db.String(20),  nullable=False, default="manual")  # manual | ai | ai_cached
    roadmap_json  = db.Column(db.Text,        nullable=False)
    status        = db.Column(db.String(20),  nullable=False, default="active")  # active | paused | completed
    created_at    = db.Column(db.DateTime, default=datetime.utcnow)

    progress = db.relationship("Progress", backref="roadmap", lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f"<RoadmapHistory {self.goal} — {self.level}>"


class CachedRoadmap(db.Model):
    """
    Stores AI-generated roadmaps permanently.
    Cache key = normalized goal + level
    When a second student enters the same career, AI is NOT called —
    the cached version is returned instantly.
    """
    __tablename__ = "cached_roadmaps"
    id           = db.Column(db.Integer, primary_key=True)
    cache_key    = db.Column(db.String(300), unique=True, nullable=False)
    goal         = db.Column(db.String(200), nullable=False)
    level        = db.Column(db.String(50),  nullable=False)
    roadmap_json = db.Column(db.Text,        nullable=False)
    hit_count    = db.Column(db.Integer,     default=1)
    created_at   = db.Column(db.DateTime, default=datetime.utcnow)
    last_used_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<CachedRoadmap {self.goal}|{self.level} hits={self.hit_count}>"


class Progress(db.Model):
    __tablename__ = "progress"
    id         = db.Column(db.Integer, primary_key=True)
    user_id    = db.Column(db.Integer, db.ForeignKey("users.id"),            nullable=False)
    roadmap_id = db.Column(db.Integer, db.ForeignKey("roadmap_history.id"),  nullable=False)
    skill_name = db.Column(db.String(200), nullable=False)
    completed  = db.Column(db.Boolean, default=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    __table_args__ = (
        db.UniqueConstraint("user_id", "roadmap_id", "skill_name", name="uq_user_roadmap_skill"),
    )

    def __repr__(self):
        return f"<Progress {self.skill_name} — {'done' if self.completed else 'pending'}>"