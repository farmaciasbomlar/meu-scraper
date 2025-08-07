from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str

@app.post("/scraper")
async def scrape(item: Item):
    return {"message": f"Hello {item.name}, scraping done!"}
