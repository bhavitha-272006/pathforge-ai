# PathForge AI 🚀

AI-Powered Personalized Career Roadmap Generator — built with Flask, Groq AI (Llama 3.1), and SQLite.

## Features

- 🤖 AI-generated roadmaps for any custom career (Groq + Llama 3.1)
- ⚡ Smart caching — AI called once per career, reused forever
- 📊 Progress tracking with real-time percentage
- 💬 AI Career Chat Assistant (context-aware)
- 📄 PDF export
- 📧 Auto-email roadmap PDF on generation
- 🌙 Dark mode
- 🎉 Confetti on 100% completion

## Tech Stack

**Backend:** Python, Flask, Flask-Login, Flask-SQLAlchemy, SQLite, Werkzeug
**AI:** Groq API, Meta Llama 3.1 (8B)
**Frontend:** HTML, CSS, JavaScript, Jinja2, Chart.js
**PDF:** ReportLab
**Email:** Gmail SMTP

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/bhavitha-272006/pathforge-ai
cd pathforge-ai
```

### 2. Install dependencies
```bash
pip install flask flask-login flask-sqlalchemy werkzeug reportlab groq python-dotenv
```

### 3. Set up environment variables
Copy `.env.example` to `.env` and fill in your own keys:
```bash
cp .env.example .env
```

Get your free Groq API key: https://console.groq.com
Get your Gmail App Password: https://myaccount.google.com/apppasswords

### 4. Run the app
```bash
python app.py
```

Open browser: http://127.0.0.1:5000

## Project Structure

```
pathforge-ai/
├── app.py              # Main Flask application
├── models.py           # Database models
├── planner.py          # Hybrid AI routing engine
├── roadmaps.py         # 30 curated roadmaps
├── ai_generator.py      # PDF generation
├── mailer.py           # Email sending
├── chat.py              # AI chat assistant
├── templates/           # HTML templates
└── static/              # CSS & JS
```

## License

This project is for educational purposes.
