# chat.py
# AI Career Chat Assistant using Groq API
# Two modes:
#   1. Roadmap chat  — context-aware, knows the student's current roadmap
#   2. General chat  — answers any career/tech question

import os
import json
from dotenv import load_dotenv

load_dotenv()

# ─────────────────────────────────────────────
#  SYSTEM PROMPTS
# ─────────────────────────────────────────────

ROADMAP_SYSTEM_PROMPT = """
You are PathForge AI Assistant — a friendly, expert career mentor embedded inside
a career roadmap learning platform.

The student is currently working on their {goal} roadmap ({level} level).
Their roadmap has these skills: {skills}
They have completed: {completed_skills} out of {total_skills} skills so far.

Your job:
- Answer questions about their roadmap, skills, topics, and resources
- Give study tips and motivation
- Explain any concept from their roadmap in simple terms
- Suggest what to focus on next based on their progress
- Answer general programming/tech questions related to their career path

Rules:
- Keep answers concise, friendly, and encouraging
- Use bullet points for lists
- If asked something unrelated to tech/career, politely redirect
- Always address the student encouragingly
- Never make up resource URLs — describe resources instead
""".strip()

GENERAL_SYSTEM_PROMPT = """
You are PathForge AI Assistant — a friendly, expert career counselor and
technical mentor for students learning tech careers.

Your job:
- Answer questions about any tech career path
- Explain programming concepts clearly
- Give study advice and learning strategies
- Help students choose between career options
- Motivate and guide students

Rules:
- Keep answers concise, clear, and beginner-friendly
- Use bullet points for structured answers
- Be encouraging and positive
- If asked something completely off-topic, politely redirect to career/tech topics
- Format code examples with proper indentation
""".strip()


# ─────────────────────────────────────────────
#  GROQ CLIENT
# ─────────────────────────────────────────────
def _get_client():
    api_key = os.environ.get("GROQ_API_KEY", "").strip()
    if not api_key:
        raise ValueError("GROQ_API_KEY missing in .env file.")
    try:
        from groq import Groq
        return Groq(api_key=api_key)
    except ImportError:
        raise ImportError("Run: pip install groq")


# ─────────────────────────────────────────────
#  ROADMAP CHAT
# ─────────────────────────────────────────────
def roadmap_chat(user_message: str, roadmap: dict,
                 progress_map: dict, history: list) -> str:
    """
    Context-aware chat about the student's current roadmap.

    Args:
        user_message : what the student typed
        roadmap      : the full roadmap dict
        progress_map : {skill_name: True/False}
        history      : list of {"role": "user"/"assistant", "content": "..."}

    Returns:
        AI response string
    """
    client = _get_client()

    # Build context
    skills = [s["name"] for s in roadmap.get("skills", [])]
    completed = [s for s, done in progress_map.items() if done]
    pending   = [s for s, done in progress_map.items() if not done]

    system = ROADMAP_SYSTEM_PROMPT.format(
        goal             = roadmap.get("goal", ""),
        level            = roadmap.get("level", ""),
        skills           = ", ".join(skills),
        completed_skills = len(completed),
        total_skills     = len(skills),
    )

    # Add pending skills context
    if pending:
        system += f"\n\nSkills still to complete: {', '.join(pending)}"
    if completed:
        system += f"\nSkills already completed: {', '.join(completed)}"

    # Build message history (last 10 messages to stay within token limits)
    messages = [{"role": "system", "content": system}]
    for msg in history[-10:]:
        messages.append({"role": msg["role"], "content": msg["content"]})
    messages.append({"role": "user", "content": user_message})

    response = client.chat.completions.create(
        model       = "llama-3.1-8b-instant",
        messages    = messages,
        temperature = 0.7,
        max_tokens  = 800,
    )
    return response.choices[0].message.content.strip()


# ─────────────────────────────────────────────
#  GENERAL CAREER CHAT
# ─────────────────────────────────────────────
def general_chat(user_message: str, history: list) -> str:
    """
    General career/tech chat — no roadmap context needed.

    Args:
        user_message : what the student typed
        history      : list of {"role": "user"/"assistant", "content": "..."}

    Returns:
        AI response string
    """
    client = _get_client()

    messages = [{"role": "system", "content": GENERAL_SYSTEM_PROMPT}]
    for msg in history[-10:]:
        messages.append({"role": msg["role"], "content": msg["content"]})
    messages.append({"role": "user", "content": user_message})

    response = client.chat.completions.create(
        model       = "llama-3.1-8b-instant",
        messages    = messages,
        temperature = 0.7,
        max_tokens  = 800,
    )
    return response.choices[0].message.content.strip()