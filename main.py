from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/agenda-hoje")
def get_agenda_hoje():
    return JSONResponse(content={"mensagem": "API do Copilot Otmiz está online e funcionando."})
