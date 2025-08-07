from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from supabase import create_client, Client
import os

# Inicializa o app FastAPI
app = FastAPI()

# Permite chamadas de fora (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo de entrada
class Item(BaseModel):
    nome: str
    preco: float
    loja: str

# Conecta com Supabase usando variáveis de ambiente
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

# Rota de teste
@app.get("/")
def read_root():
    return {"message": "Está funcionando com Supabase!"}

# Rota para salvar item no Supabase
@app.post("/scraper")
async def scrape(item: Item):
    data = {
        "nome": item.nome,
        "preco": item.preco,
        "loja": item.loja
    }
    result = supabase.table("produtos").insert(data).execute()
    return {"message": "Dados salvos com sucesso no Supabase!"}
