from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="TimeSaver API")
app.include_router(router)

@app.get("/")
def home():
    return {"mensagem": "Bem-vindo à TimeSaver API! Envie tarefas em /organizar"}