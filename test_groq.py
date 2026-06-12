# test_groq.py
# Run this file directly to test if Groq is working:
#   python test_groq.py

import os
import json
from dotenv import load_dotenv

load_dotenv()

print("=" * 50)
print("STEP 1 — Checking .env file")
print("=" * 50)

api_key = os.environ.get("GROQ_API_KEY", "")

if not api_key:
    print("❌ GROQ_API_KEY not found!")
    print("   Fix: Make sure your .env file exists in THIS folder")
    print("   and contains:  GROQ_API_KEY=gsk_xxxxxxxxxxxx")
    exit()
elif api_key == "paste_your_groq_key_here":
    print("❌ You forgot to replace the placeholder!")
    print("   Fix: Open .env and replace 'paste_your_groq_key_here'")
    print("   with your actual key from https://console.groq.com")
    exit()
else:
    print(f"✅ API key found: {api_key[:8]}{'*' * 20}")

print()
print("=" * 50)
print("STEP 2 — Testing Groq import")
print("=" * 50)

try:
    from groq import Groq
    print("✅ groq package installed")
except ImportError:
    print("❌ groq not installed!")
    print("   Fix: Run this command:  pip install groq")
    exit()

print()
print("=" * 50)
print("STEP 3 — Calling Groq API for 'Cloud Computing'")
print("=" * 50)

try:
    client = Groq(api_key=api_key)

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant. Return ONLY valid JSON, nothing else."
            },
            {
                "role": "user",
                "content": (
                    "Generate a learning roadmap JSON for Cloud Computing beginner level, 3 months, 2 hours/day.\n"
                    "Return ONLY this JSON structure, no other text:\n"
                    '{"goal":"Cloud Computing","level":"Beginner","duration":"3 months",'
                    '"hours_per_day":2,"source":"ai","skills":[{"name":"skill name",'
                    '"duration":"1 week","topics":["t1","t2"],"tasks":["task1"],'
                    '"resources":[{"title":"name","url":"https://example.com"}]}]}'
                )
            }
        ],
        temperature=0.3,
        max_tokens=2000,
    )

    raw = response.choices[0].message.content
    print(f"✅ Groq responded!")
    print(f"\n--- RAW RESPONSE ---")
    print(raw[:500])
    print("--- END ---\n")

    # Try parsing
    import re
    cleaned = raw.strip()
    cleaned = re.sub(r'^```(?:json)?\s*', '', cleaned)
    cleaned = re.sub(r'\s*```$', '', cleaned)
    cleaned = cleaned.strip()
    match = re.search(r'\{.*\}', cleaned, re.DOTALL)
    if match:
        cleaned = match.group(0)

    data = json.loads(cleaned)
    print(f"✅ JSON parsed successfully!")
    print(f"   Goal: {data.get('goal')}")
    print(f"   Skills: {len(data.get('skills', []))}")
    print()
    print("🎉 Everything is working! Groq AI generation is ready.")

except json.JSONDecodeError as e:
    print(f"❌ JSON parse failed: {e}")
    print("   The AI returned something that isn't valid JSON.")
    print("   This is rare — just try running again.")

except Exception as e:
    print(f"❌ Groq API call failed!")
    print(f"   Error: {e}")
    print()
    err = str(e).lower()
    if "auth" in err or "api key" in err or "invalid" in err:
        print("   Fix: Your API key is wrong or expired.")
        print("   Get a new one from https://console.groq.com → API Keys")
    elif "rate" in err or "limit" in err:
        print("   Fix: Rate limit hit. Wait 1 minute and try again.")
    elif "connect" in err or "network" in err or "timeout" in err:
        print("   Fix: No internet connection or Groq is down.")
        print("   Check your internet and try again.")
    else:
        print("   Unknown error. Share this message for help.")