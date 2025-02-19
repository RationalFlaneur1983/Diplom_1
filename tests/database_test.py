import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from praktikum.database import Database


# Проверяем, что метод available_buns возвращает 3 булочки
def test_available_buns_count(db):
    assert len(db.available_buns()) == 3

# Проверяем, что метод available_ingredients возвращает 6 ингредиентов
def test_available_ingredients_count(db):
    assert len(db.available_ingredients()) == 6

# Проверяем, что метод available_buns возвращает список булочек
def test_available_buns_return_type(db):
    buns = db.available_buns()
    assert isinstance(buns, list)
    assert all(isinstance(bun, Bun) for bun in buns)

# Проверяем, что метод available_ingredients возвращает список ингредиентов
def test_available_ingredients_return_type(db):
    ingredients = db.available_ingredients()
    assert isinstance(ingredients, list)
    assert all(isinstance(ingredient, Ingredient) for ingredient in ingredients)
