# EduGenie - Google Gemini Powered Learning Assistant

Features: Q&A, topic explanation, 3-question MCQ quiz, summarization, and personalized learning path.

## Windows
1. `python -m venv .venv`
2. `\.venv\Scripts\python.exe -m pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and add your Gemini API key.
4. `\.venv\Scripts\python.exe -m uvicorn main:app --host 127.0.0.1 --port 8000`
5. Open http://127.0.0.1:8000

If PowerShell blocks activation, do not activate the environment; use the direct Python path above.

`ALLOW_DEMO_FALLBACK=true` keeps all five features usable when Gemini is missing, unavailable, or quota-limited. With a working Gemini key/quota, the features use Gemini.
