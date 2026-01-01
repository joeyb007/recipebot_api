import joblib
from pathlib import Path


MODEL_DIR = Path(__file__).parent
vectorizer = joblib.load(MODEL_DIR / f"tfidf_vectorizer.joblib")

def load_vectorizer():
    return vectorizer