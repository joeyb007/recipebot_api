import re

# It seems to make the most sense to use:
#   'keyword' in string
# However, this doesn't account for edge-cases
# For example, "Ham" in "Hamburger."
# Note that all strings have already been lowercased

def containsPork(string):
    pork_pattern = r"\b(bacon|ham|prosciutto|pancetta|salami|sausage|chorizo)\b"
    if re.search(pork_pattern, string):
        return True
    return False

def containsBeef(string):
    beef_pattern = r"\b(beef|steak|ground beef|corned beef|brisket)\b"
    if re.search(beef_pattern, string):
        return True
    return False

def containsChicken(string):
    chicken_pattern = r"\b(chicken|drumstick|thigh|breast|poultry)\b"
    if re.search(chicken_pattern, string):
        return True
    return False

def containsFish(string):
    fish_pattern = r"\b(fish|salmon|tuna|cod|shrimp|crab|lobster|scallop|clams|mussels)\b"
    if re.search(fish_pattern, string):
        return True
    return False

def containsEggs(string):
    egg_pattern = r"\b(egg|eggs|whites|yolk)\b"
    if re.search(egg_pattern, string):
        return True
    return False

def containsDairy(string):
    dairy_pattern = r"\b(milk|cheese|butter|cream|yogurt|ghee)\b"
    if re.search(dairy_pattern, string):
        return True
    return False

def containsHoney(string):
    honey_pattern = r"\b(honey)\b"
    if re.search(honey_pattern, string):
        return True
    return False

def isVegetarian(string):
    if not (containsPork(string) and 
            containsBeef(string) and 
            containsChicken(string) and containsFish(string)):
        return True
    return False

def isVegan(string):
    if isVegetarian(string) and not (containsDairy(string) and containsEggs(string)):
        return True
    return False

def containsNuts(string):
    nuts_pattern = r"\b(almond|almonds|cashew|cashews|peanut|peanuts|walnut|walnuts|pecan|pecans|hazelnut|filbert|filberts|pistachio|pistachios|macadamia|brazil nut|brazil nuts)\b"
    if re.search(nuts_pattern, string):
        return True
    return False

def containsPeanuts(string):
    peanuts_pattern = r"b(peanut|peanuts)\b"
    if re.search(peanuts_pattern, string):
        return True
    return False