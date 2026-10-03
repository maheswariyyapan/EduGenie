import json, re
from pydantic import ValidationError
from schemas import QuizQuestion
from services.gemini_client import GeminiUnavailable, generate_text
SYSTEM_PROMPT="You are EduGenie's quiz generator. Create educational MCQs. Each question must have exactly 4 options, one correct answer, and a short explanation."
def clean_json_block(raw):
    text=raw.strip(); text=re.sub(r'^```(?:json)?\s*','',text,flags=re.I); text=re.sub(r'\s*```$','',text); return text.strip()
def normalize_questions(data):
    if isinstance(data,dict): data=data.get('questions',[])
    if not isinstance(data,list): raise ValueError('Quiz response must contain a list.')
    out=[]
    for item in data:
        if not isinstance(item,dict): continue
        opts=item.get('options',[]); ans=str(item.get('answer','')).strip()
        if not isinstance(opts,list): continue
        opts=[str(x).strip() for x in opts if str(x).strip()]
        if len(opts)!=4: continue
        if ans.isdigit() and 0<int(ans)<=4: ans=opts[int(ans)-1]
        if ans not in opts: continue
        q=str(item.get('question','')).strip()
        if not q: continue
        out.append(QuizQuestion(question=q, options=opts, answer=ans, explanation=str(item.get('explanation','')).strip()))
    if not out: raise ValueError('No valid quiz questions were returned.')
    return out
def demo_quiz(text,count):
    base=[('What is the best way to learn a new concept?',['Understand it','Skip it','Ignore examples','Avoid practice'],0),('What should you do after learning a concept?',['Practice it','Forget it','Avoid questions','Skip revision'],0),('Why are examples useful?',['They connect ideas to practice','They remove learning','They make notes unnecessary','They prevent revision'],0)]
    return [QuizQuestion(question=q,options=o,answer=o[i],explanation='Understanding and practice reinforce learning.') for q,o,i in base[:count]]
async def generate_quiz(text,count=3):
    prompt=f'Create exactly {count} MCQs from this educational text. Return ONLY JSON with questions, each containing question, options (4), answer (exact option), explanation.\n\nTEXT:\n{text}'
    try:
        raw=await generate_text(prompt,system_instruction=SYSTEM_PROMPT,temperature=0.3,max_output_tokens=3000,json_mode=True)
        return normalize_questions(json.loads(clean_json_block(raw)))[:count]
    except GeminiUnavailable:
        return demo_quiz(text,count)
    except (json.JSONDecodeError,ValueError,ValidationError) as error:
        raise RuntimeError(f'Could not parse quiz response: {error}') from error
