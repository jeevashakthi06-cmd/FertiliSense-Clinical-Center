"""
FertiCare AI — Backend API
---------------------------
A small Flask API that the web frontend (or a WhatsApp webhook, later)
talks to. It owns:
- The FertiCare AI persona/system prompt
- Per-session conversation memory
- The actual call to the Anthropic API (your key never touches the browser)

Run:
    pip install -r requirements.txt
    cp .env.example .env      # then fill in your ANTHROPIC_API_KEY
    python app.py

The frontend (../frontend/index.html) is configured to call
http://localhost:5000/api/chat by default.
"""

import os
import uuid
from pathlib import Path

import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)  # allow the frontend (served from a different origin/file) to call this API

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
MODEL = os.getenv("ANTHROPIC_MODEL", "claude-sonnet-4-6")
ANTHROPIC_URL = "https://api.anthropic.com/v1/messages"

SYSTEM_PROMPT = Path(__file__).with_name("system_prompt.txt").read_text(encoding="utf-8")

# In-memory conversation store, keyed by session_id.
# Replace with Redis/Postgres before running multiple server workers or
# deploying to production — this resets whenever the process restarts.
SESSIONS = {}

MAX_HISTORY_MESSAGES = 30  # keep token usage/cost bounded


@app.route("/api/session", methods=["POST"])
def create_session():
    """Frontend calls this once when the page loads to get a session_id."""
    session_id = str(uuid.uuid4())
    SESSIONS[session_id] = []
    return jsonify({"session_id": session_id})


@app.route("/api/chat", methods=["POST"])
def chat():
    body = request.get_json(force=True, silent=True) or {}
    session_id = body.get("session_id")
    user_message = (body.get("message") or "").strip()

    if not session_id or session_id not in SESSIONS:
        return jsonify({"error": "Invalid or missing session_id. Call /api/session first."}), 400

    if not user_message:
        return jsonify({"error": "message is required"}), 400

    if not ANTHROPIC_API_KEY:
        return jsonify({
            "reply": "[DEV MODE — no ANTHROPIC_API_KEY set on the server] "
                      f"Would send to Claude: {user_message!r}"
        })

    history = SESSIONS[session_id]
    history.append({"role": "user", "content": user_message})
    history[:] = history[-MAX_HISTORY_MESSAGES:]

    try:
        resp = requests.post(
            ANTHROPIC_URL,
            headers={
                "x-api-key": ANTHROPIC_API_KEY,
                "anthropic-version": "2023-06-01",
                "Content-Type": "application/json",
            },
            json={
                "model": MODEL,
                "max_tokens": 1000,
                "system": SYSTEM_PROMPT,
                "messages": history,
            },
            timeout=30,
        )
        resp.raise_for_status()
        data = resp.json()
        reply = "\n".join(
            block["text"] for block in data.get("content", []) if block.get("type") == "text"
        ).strip() or "Sorry, I couldn't generate a response just now."

    except requests.exceptions.RequestException as e:
        print("Anthropic API error:", e)
        return jsonify({"error": "Upstream API error. Please try again."}), 502

    history.append({"role": "assistant", "content": reply})
    return jsonify({"reply": reply})


@app.route("/api/reset", methods=["POST"])
def reset():
    body = request.get_json(force=True, silent=True) or {}
    session_id = body.get("session_id")
    if session_id in SESSIONS:
        SESSIONS[session_id] = []
    return jsonify({"ok": True})


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(port=5000, debug=True)
