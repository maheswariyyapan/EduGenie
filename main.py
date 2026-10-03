from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from schemas import TextRequest, ExplainRequest, QuizRequest, LearnRequest, QAResponse, TextResponse, QuizResponse, HealthResponse
from qna import answer_question
from explanation_module import explain_topic
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations
app = FastAPI(title="EduGenie - AI Learning Assistant", version="1.0.0", description="Google Gemini powered educational assistant")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")
@app.get("/health", response_model=HealthResponse)
async def health():
    return HealthResponse(status="ok", service="EduGenie")
@app.post("/qa", response_model=QAResponse)
async def qa(payload: TextRequest):
    return QAResponse(answer=await answer_question(payload.text))
@app.post("/explain", response_model=TextResponse)
async def explain(payload: ExplainRequest):
    return TextResponse(result=await explain_topic(payload.topic))
@app.post("/quiz", response_model=QuizResponse)
async def quiz(payload: QuizRequest):
    return QuizResponse(questions=await generate_quiz(payload.text, payload.count))
@app.post("/summarize", response_model=TextResponse)
async def summarize(payload: TextRequest):
    return TextResponse(result=await summarize_text(payload.text))
@app.post("/learn/recommendations", response_model=TextResponse)
async def learning_recommendations(payload: LearnRequest):
    return TextResponse(result=await get_learning_recommendations(payload.topic, payload.level))
