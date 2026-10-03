from services.gemini_client import GeminiUnavailable, generate_text
def demo_explanation(topic):
    return f"Definition:\n{topic} is a concept that can be understood by learning what it means, how it works, and where it is used.\n\nWhy it is important:\nUnderstanding {topic} helps you learn related concepts.\n\nKey points:\n• Learn the basic definition.\n• Understand the main components or steps.\n• Study a simple example.\n• Practice the concept.\n\nExample:\nConnect {topic} to a simple real-world or programming example.\n\nRecap:\nLearn the definition, understand the working, and practice an example."
async def explain_topic(topic):
    prompt=f"Explain this academic topic to a beginner. Topic: {topic}. Use Definition, Why it is important, Key points, Example, and Recap."
    try:
        return await generate_text(prompt, system_instruction="You are EduGenie's concept explanation tutor. Use simple English without losing correctness.", temperature=0.3, max_output_tokens=1600)
    except GeminiUnavailable:
        return demo_explanation(topic)
