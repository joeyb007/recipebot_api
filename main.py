from fastapi import FastAPI
from schemas import RecipeRequest, RecipeResponse
import json

app = FastAPI()


    


@app.post('/get_new_recipe', response_model=RecipeResponse)
async def get_new_recipe():
    return {"Message": "Hello, world"}