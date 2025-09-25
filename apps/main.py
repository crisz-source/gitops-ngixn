from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Operacao(BaseModel):
    a: float
    b: float

@app.get("/")
def home():
    return {"status": "ok"}

@app.post("/soma")
def somar(op: Operacao):
    return {"resultado": op.a + op.b}

@app.post("/subtracao")
def subtrair(op: Operacao):
    return {"resultado": op.a - op.b}
