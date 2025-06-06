from fastapi import FastAPI
from random import randint


app = FastAPI()


@app.get("/")
async def get_random_percentage():
    return {'percentage': randint(0, 100)}
