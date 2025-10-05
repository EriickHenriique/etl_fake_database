from fastapi import FastAPI
from backend.fake_generate import database_random

app = FastAPI()

@app.get("/gerar_compra")
async def root():
    return database_random()



