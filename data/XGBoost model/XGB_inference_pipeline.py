# Now, we need to put all of the steps within each notebook together to produce a repeatable pipeline:
# Pipeline function model:
# Preprocess Data -> Vectorize -> XGB inference -> Return

# 1. Preprocess

def preprocess_ingredients(list_of_ingredients):
    return ' '.join(list_of_ingredients)

# 2. Vectorize