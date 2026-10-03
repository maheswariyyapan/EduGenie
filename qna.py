from services.gemini_client import GeminiUnavailable, generate_text
def demo_answer(question):
    return f"Demo answer for: {question}\n\nEduGenie is running correctly, but Gemini is currently unavailable or its quota is exhausted. Add a working Gemini API key/quota for live AI answers."
async def answer_question(question):
    prompt=f"Answer this student question in simple English. Question: {question}"
    try:
        return await generate_text(prompt, system_instruction="You are EduGenie, an accurate and friendly AI learning assistant. Always use simple English.", temperature=0.3, max_output_tokens=1200)
    except GeminiUnavailable:
        return demo_answer(question)
