from fastapi import FastAPI

aplicação = FastAPI()

@aplicação.get("/agenda-hoje")
def ler_agenda():
    return {"mensagem": "Agenda de hoje lida com sucesso"}
