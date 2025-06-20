from fastapi import FastAPI

app = FastAPI()

@app.get("/agenda-hoje")
def ler_agenda():
    return {"mensagem": "Agenda de hoje lida com sucesso"}

