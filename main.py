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

if __name__ == "__main__":
    import uvicorn
    import os
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)