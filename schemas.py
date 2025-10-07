# Outlines JSON type schemas for requests and responses
from pydantic import BaseModel
from typing import List, Dict

class RecipeRequest(BaseModel):
    ingredients: List[str]
    restrictions: List[str]
    preferences: List[str]

class Nutrition(BaseModel):
    calories: float
    protein: float
    fat: float
    carbs: float

class RecipeResponse(BaseModel):
    title: str
    ingredients: List[str]
    estimated_time: float
    instructions: List[str]
    restrictions: List[str]
    nutrition: Nutrition