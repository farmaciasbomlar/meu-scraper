from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import os
import subprocess
import uuid

app = FastAPI()

# Permitir chamadas externas (Lovable)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "API Ativa e funcionando"}

@app.post("/upload-planilha")
async def upload_planilha(file: UploadFile = File(...)):
    # Salva arquivo temporariamente
    input_filename = f"input_{uuid.uuid4().hex}.xlsx"
    output_filename = f"output_{uuid.uuid4().hex}.xlsx"

    with open(input_filename, "wb") as f:
        f.write(await file.read())

    # Executa o script com o arquivo salvo
    try:
        subprocess.run(
            ["python", "amazon_scraper.py", "--input", input_filename, "--output", output_filename, "--headless"],
            check=True
        )
    except subprocess.CalledProcessError as e:
        return {"error": "Erro ao executar o script", "detalhes": str(e)}

    # Retorna o arquivo processado
    return FileResponse(output_filename, media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', filename="resultado.xlsx")
