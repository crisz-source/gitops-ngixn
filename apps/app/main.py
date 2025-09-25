from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()

templates = Jinja2Templates(directory="templates")

class Operacao(BaseModel):
    a: float
    b: float

@app.get("/", response_class=HTMLResponse)
async def get_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/soma")
def somar(op: Operacao):
    return {"resultado": op.a + op.b}

@app.post("/subtracao")
def subtrair(op: Operacao):
    return {"resultado": op.a - op.b}