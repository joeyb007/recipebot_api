# This file contains functions that, given a list of strings (ingredients), checks
# whether the recipe complies with a given dietary restriction. This will be used to
# manually label data that will be used to fine-tune a more robust classification system

import re

# It might initially seem to make the most sense to use:
#   "'keyword' in string"?
# However, this doesn't account for edge-cases
# For example, "Ham" in "Hamburger."
# Note that all strings have already been lowercased in preprocessing.


# given a regex pattern, returns a predicate that loops over a list
# of ingredients, checking whether any of them contain the provided pattern
# Requires: string argument evaluates to a valid Regex pattern
# make-contains-fn: string -> (list[string] -> Bool)

def make_contains_fn(pattern):
    compiled = re.compile(pattern)
    def contains(ingredients):
        for ingredient in ingredients:
            if compiled.search(ingredient):
                return True
            return False
    return contains


# Defining common ingredient classes and associated regex patterns 
PATTERNS = {
    "pork": r"\b(bacon|ham|prosciutto|pancetta|salami|sausage|chorizo)\b",
    "beef": r"\b(beef|steak|ground beef|corned beef|brisket)\b",
    "chicken": r"\b(chicken|drumstick|thigh|breast|poultry)\b",
    "fish": r"\b(fish|salmon|tuna|cod|shrimp|crab|lobster|scallop|clams|mussels)\b",
    "eggs": r"\b(egg|eggs|whites|yolk)\b",
    "dairy": r"\b(milk|cheese|butter|cream|yogurt|ghee)\b",
    "honey": r"\b(honey)\b",
    "nuts": r"\b(almond|almonds|cashew|cashews|peanut|peanuts|walnut|walnuts|pecan|pecans|hazelnut|filbert|filberts|pistachio|pistachios|macadamia|brazil nut|brazil nuts)\b",
    "peanuts": r"\b(peanut|peanuts)\b",
    "high-carb": r"\b(sugar|flour|rice|pasta|potato|corn|oats|beans)\b",
    "gluten": r"\b(wheat|flour|barley|rye|semolina|breadcrumbs|malt)\b",
    "soy": r"\b(soy|soy sauce|tofu|edamame|soybean|miso)\b",
    "shellfish": r"\b(shrimp|crab|lobster|mussels|clams|scallops|prawns|oysters)\b",
    "sesame": r"\b(sesame|tahini|sesame seeds|sesame oil)\b",
    "alcohol": r"\b(beer|wine|vodka|rum|whiskey|tequila)\b",
    "processed_meats": r"\b(bacon|salami|ham|sausage|chorizo|hot dog|pepperoni)\b",
    "legumes": r"\b(lentil|chickpea|kidney bean|black bean|navy bean|soybean|pea)\b"
}

# Creates a dictionary of ingredients and functions to check for them. 
PATTERN_FUNCTIONS = {name:make_contains_fn(pattern) for name, pattern in PATTERNS}

# Adding isVegan, isVegetarian, and isKeto