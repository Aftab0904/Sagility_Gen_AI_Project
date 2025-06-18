from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from utils.llm_handler import generate_response

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/classify_email", response_class=HTMLResponse)
async def classify_email(request: Request, email_content: str = Form(...)):
    response = generate_response(email_content)
    return templates.TemplateResponse("index.html", {"request": request, "email_content": email_content, "response": response})