from services.gemini_client import GeminiUnavailable, generate_text
SYSTEM_PROMPT="You are EduGenie's educational summarization assistant. Keep important information, remove repetition, use simple English, preserve meaning, and make the result useful for exam revision."
def demo_summary(text):
    return f"Short Summary\n{' '.join(text.split())[:500]}\n\nKey Points\n• Identify the main idea.\n• Note important concepts and definitions.\n• Review examples and applications.\n\nImportant Terms\n• Main topic\n• Key concept\n\nDemo mode: Gemini is unavailable or quota is exhausted."
async def summarize_text(text):
    try:
        return await generate_text(f"Summarize this educational passage. Give Short Summary, 3-7 Key Points, and Important Terms.\n\n{text}", system_instruction=SYSTEM_PROMPT, temperature=0.2, max_output_tokens=1600)
    except GeminiUnavailable:
        return demo_summary(text)
