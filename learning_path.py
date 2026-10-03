from services.gemini_client import GeminiUnavailable, generate_text
SYSTEM_PROMPT="You are EduGenie's personalized learning-path assistant. Create practical learning plans in simple English. Do not invent specific URLs."
def demo_learning_path(topic, level):
    return f"Learning Goal\nLearn {topic} from the {level} level.\n\nPrerequisites\nBasic computer knowledge and willingness to practice.\n\nBeginner Stage\nLearn definitions, basic concepts, and simple examples.\n\nIntermediate Stage\nPractice common problems and build a small project.\n\nAdvanced Stage\nStudy advanced concepts and build a larger project.\n\nSuggested Timeline\n2 to 4 weeks with regular practice.\n\nPractice Projects\nBuild a small project related to {topic}.\n\nRevision Plan\nReview notes weekly and solve practice questions.\n\nRecommended Resources\nUse class notes, textbooks, official documentation, and trusted learning platforms.\n\nFinal Advice\nPractice a little every day and increase difficulty gradually.\n\nDemo mode: Gemini is unavailable or quota is exhausted."
async def get_learning_recommendations(topic, level="beginner"):
    try:
        return await generate_text(f"Create a personalized learning path for {topic}. Current level: {level}. Include Learning Goal, Prerequisites, Beginner Stage, Intermediate Stage, Advanced Stage, Suggested Timeline, Practice Projects, Revision Plan, Recommended Resources, and Final Advice.", system_instruction=SYSTEM_PROMPT, temperature=0.5, max_output_tokens=2600)
    except GeminiUnavailable:
        return demo_learning_path(topic, level)
