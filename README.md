# FertiCare AI — Frontend + Backend

A WhatsApp-styled fertility lifestyle assistant, split into two independent
pieces so it can run on your own machine (or be deployed) with your own API
key:

```
ferticare-app/
├── frontend/
│   └── index.html        ← the chat webpage (WhatsApp look & feel)
└── backend/
    ├── app.py             ← Flask API: holds the persona, memory, and the
    │                        actual call to Claude
    ├── system_prompt.txt  ← the FertiCare AI persona (edit this to tune tone)
    ├── requirements.txt
    └── .env.example
```

**Why split it this way?** The frontend never sees your API key — it only
talks to your backend, and your backend is the only thing that talks to
Anthropic. This is the same shape a real production app would use.

## 1. Run the backend

```bash
cd backend
pip install -r requirements.txt
cp .env.example .env
```

Open `.env` and add your own Anthropic API key:
```
ANTHROPIC_API_KEY=sk-ant-...
ANTHROPIC_MODEL=claude-sonnet-4-6
```

Then start it:
```bash
python app.py
```

You should see `Running on http://127.0.0.1:5000`. Leave this running.

If you don't have a key yet, that's fine — leaving `ANTHROPIC_API_KEY` blank
puts the backend in **dev mode**: it responds with a placeholder message
instead of calling the API, so you can test that everything is wired up
correctly first.

## 2. Open the frontend

Just double-click `frontend/index.html` to open it in your browser — no
build step, no server needed for the frontend itself. It's already
configured to call `http://localhost:5000`, which is where the backend
from step 1 is listening.

You should see the chat open, say "connecting...", then greet you and ask
its first question.

## 3. Test it

Try a few turns — age, height, weight, sleep, stress, etc. Once enough
info is collected, it should return the structured "🌸 Fertility Lifestyle
Summary" format from the persona. Use the **Restart** button in the header
to clear the conversation and start over.

## 4. Deploying for real (optional)

- **Backend**: deploy `backend/` to Render, Railway, Fly.io, or similar.
  Set `ANTHROPIC_API_KEY` as an environment variable there (never commit
  your real `.env` file).
- **Frontend**: once the backend has a real URL (e.g.
  `https://your-app.onrender.com`), update the `BACKEND_URL` constant near
  the top of `frontend/index.html`'s `<script>` block, then host the HTML
  file anywhere static (GitHub Pages, Netlify, Vercel, or even just email
  it to someone).
- **Production notes**: the backend currently keeps conversation history
  in memory (`SESSIONS` dict in `app.py`) — this resets on restart and
  won't work correctly across multiple server workers. Swap in
  Redis/Postgres before real usage. Also add basic rate limiting per
  session before making this public.

## 5. Connecting to real WhatsApp later

This backend's `/api/chat` logic is the same shape you'd reuse for a real
WhatsApp Business Cloud API webhook (receive message → look up session →
call Claude → send reply) — see the earlier `whatsapp-fertility-bot-v2`
project for a webhook version of this same backend if you want to go that
route.
