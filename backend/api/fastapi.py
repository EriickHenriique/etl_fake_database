from fastapi import FastAPI
from backend.data.fake_generate import database_random

#Chamando a Classe
app = FastAPI()


#Criando API com retorno da Fake Database
@app.get("/gerar_compra/{param}")
async def gerar_compra(param: int):
 
    if param < 1:
        return {"error": "Número de Compras deve ser pelo menos 1"}
    
    return database_random(param)