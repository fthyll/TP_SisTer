from fastapi import FastAPI
import uvicorn
from mylib.logic import search_wiki, wiki, phrase

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Wikipedia API. Call /search or /wiki"}


@app.get("/search/{value}")
async def search(value: str):
    """Mencari laman di Wikipedia"""
    result = search_wiki(value)
    return {"result": result}


@app.get("/wiki/{name}")
async def get_wiki(name: str):
    """Mengambil laman dari Wikipedia"""
    result = wiki(name)
    return {"result": result}


@app.get("/phrase/{name}")
async def get_phrase(name: str):
    """Mengambil laman dari Wikipedia dan mengembalikan kalimat"""
    result = phrase(name)
    return {"result": result}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
