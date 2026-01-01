# Now, we need to put all of the steps within each notebook together to produce a repeatable pipeline:
# Pipeline function model:
# Preprocess Data -> Vectorize -> XGB inference -> Return
from models.Vectorizers.load_vectorizer import load_vectorizer
from models.XGB_models.load_XGB import load_models

vectorizer = load_vectorizer()
models = load_models()

def classify_ingredients(list_of_ingredients):
    # 1. Preprocess
    ingredients_string = ' '.join(list_of_ingredients).lower()
    # 2. Vectorize
    vectorized_ingredients = vectorizer.transform([ingredients_string])
    # 3. XGB inference
    results = {}
    for label, model in models.items():
        X = vectorized_ingredients
        prob = model.predict_proba(X)[0,1]
        results[label] = 1 if prob >= 0.4 else 0
    # 4. Return
    return results


if __name__ == '__main__':
    res = classify_ingredients(["pancetta", "egg yolk", "cheese"])
    print(res)