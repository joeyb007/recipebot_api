from fastapi import FastAPI
from schemas import RecipeRequest, RecipeResponse
import json

app = FastAPI()

@app.post('/get_new_recipe', response_model=RecipeResponse)
async def get_new_recipe():
    return {"Message": "Hello, world"}


# XGBoost inference endpoint
from pipelines.XGB_inference_pipeline import classify_ingredients
from schemas import IngredientInferenceRequest, IngredientInferenceResponse


@app.post('/ingredient_inference', response_model=IngredientInferenceResponse)
async def ingredient_inference(request: IngredientInferenceRequest):
    forbidden_ingredients = request.ingredients
    return classify_ingredients(forbidden_ingredients)