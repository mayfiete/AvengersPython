
from fastapi import FastAPI

app = FastAPI()


@app.get("/heroes", tags=["heroes"])
async def get_heroes() -> dict:
    return {"heroes": [{"name": "Deadpool"}, {"name": "Superman"}]}


# uvicorn heroes_endpoint:app --port 8000 --reload