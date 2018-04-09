from recipeGenerator import *

shoppingList = []

def addToList(*items):
    for item in items:
        shoppingList.append(item)

    return shoppingList



thingsToBuy = amountOfIngredients(6)
print addToList(thingsToBuy)
