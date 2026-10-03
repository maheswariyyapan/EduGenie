import asyncio
from dotenv import load_dotenv
from google import genai
from google.genai import types
from config import ALLOW_DEMO_FALLBACK, GEMINI_API_KEY, GEMINI_MODEL
load_dotenv()
_client = None
class GeminiUnavailable(RuntimeError):
    pass
def _get_client():
    global _client
    if _client is None:
        if not GEMINI_API_KEY:
            raise GeminiUnavailable("GEMINI_API_KEY is missing")
        _client = genai.Client(api_key=GEMINI_API_KEY)
    return _client
def _generate_sync(prompt, system_instruction, temperature, max_output_tokens, json_mode):
    kwargs = {"temperature": temperature, "max_output_tokens": max_output_tokens}
    if system_instruction:
        kwargs["system_instruction"] = system_instruction
    if json_mode:
        kwargs["response_mime_type"] = "application/json"
    response = _get_client().models.generate_content(model=GEMINI_MODEL, contents=prompt, config=types.GenerateContentConfig(**kwargs))
    text = getattr(response, "text", None)
    if not text:
        raise RuntimeError("Gemini returned an empty response.")
    return text.strip()
async def generate_text(prompt: str, system_instruction: str | None = None, temperature: float = 0.3, max_output_tokens: int = 1200, json_mode: bool = False) -> str:
    try:
        return await asyncio.to_thread(_generate_sync, prompt, system_instruction, temperature, max_output_tokens, json_mode)
    except Exception as error:
        print(f"Gemini API Error: {error}")
        if ALLOW_DEMO_FALLBACK:
            raise GeminiUnavailable(str(error)) from error
        raise RuntimeError(f"Gemini API request failed: {error}") from error
