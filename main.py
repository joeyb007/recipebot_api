from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()

class IngredientsInput(BaseModel):
    ingredients: list[str]

@app.post('/get_new_recipe')
async def get_new_recipe():
    return {"Message": "Hello, world"}