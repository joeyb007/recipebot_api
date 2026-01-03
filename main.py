from fastapi import FastAPI, HTTPException, status
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
    if not request.ingredients:
        raise HTTPException(
            status_code=400,
            detail="Ingredients list must be nonempty"
        )
    forbidden_ingredients = request.ingredients
    if len(forbidden_ingredients) > 100:
        raise HTTPException(
            status_code=413,
            detail='Request payload too large; ingredient list exceeds 100 items.'
        )
    return classify_ingredients(forbidden_ingredients)