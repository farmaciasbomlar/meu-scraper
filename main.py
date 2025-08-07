from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str

@app.post("/scraper")
async def scrape(item: Item):
    return {"message": f"Hello {item.name}, scraping done!"}

@app.get("/")
def read_root():
    return {"message": "Está funcionando!"}

# Adicione isso no final:
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=10000)
