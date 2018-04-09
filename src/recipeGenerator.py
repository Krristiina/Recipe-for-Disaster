import json
import random

with open('../resources/ingredientsTagged.json') as ingredientData:
    ingredients = json.load(ingredientData)

def amountOfIngredients(numberOfIngredients):
    ingredientList = []
    for i in range(numberOfIngredients):
        ingredient = random.choice(ingredients)
        ingredientList.append(ingredient["name"])

    return ingredientList


print amountOfIngredients(6)