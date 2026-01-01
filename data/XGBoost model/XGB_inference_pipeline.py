# Now, we need to put all of the steps within each notebook together to produce a repeatable pipeline:
# Pipeline function model:
# Preprocess Data -> Vectorize -> XGB inference -> Return


def classify_ingredients(list_of_ingredients):
    # 1. Preprocess
    ingredients_string = ' '.join(list_of_ingredients)
    # 2. Vectorize

# 1. Preprocess

# 2. Load models (for vectorization + XGB inference)
from models.