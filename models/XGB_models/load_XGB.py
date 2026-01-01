import joblib
from pathlib import Path

MODEL_DIR = Path(__file__).parent

labels = ['alcohol', 'beef', 'chicken', 'dairy', 'eggs',
          'fish', 'gluten', 'high_carb', 'honey', 'legumes',
          'nuts', 'peanuts', 'pork', 'processed_meats', 'sesame',
          'shellfish', 'soy', 'sugar']

models = {}

def load_models():
    for label in labels:
        models[label] = joblib.load(MODEL_DIR / f"{label}_xgboost.joblib")
    
    return models