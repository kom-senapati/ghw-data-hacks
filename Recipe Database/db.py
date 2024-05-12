from sqlobject import *
import os
import requests

db_filename = os.path.abspath("database.db")
connection_string = "sqlite:" + db_filename
connection = connectionForURI(connection_string)
sqlhub.processConnection = connection


class Recipe(SQLObject):
    name = StringCol()
    ingredients = StringCol()
    instructions = StringCol()


Recipe.createTable(ifNotExists=True)


def add_recipe(name, ingredients, instructions):
    Recipe(name=name, ingredients=ingredients, instructions=instructions)


def get_recipes():
    return Recipe.select()


def get_recipe(name):
    return Recipe.selectBy(name=name).getOne()


def delete_recipe(name):
    Recipe.deleteBy(name=name)
    return True if Recipe.selectBy(name=name).count() == 0 else False


def add_recipe_api(name):
    response = requests.get(
        f"https://www.themealdb.com/api/json/v1/1/search.php?s={name}"
    )

    if not response.status_code == 200:
        return None

    data = response.json()
    recipe = data["meals"][0]
    ingredients = []
    for i in range(1, 21):
        ingredient = recipe[f"strIngredient{i}"]
        if ingredient:
            ingredients.append(ingredient)
    ingredients = ", ".join(ingredients)
    instructions = recipe["strInstructions"]
    add_recipe(name, ingredients, instructions)
    return recipe
