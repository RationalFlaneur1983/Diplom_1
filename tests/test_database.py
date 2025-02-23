import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from helpers.helpers import Helpers
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from praktikum.database import Database

class TestDatabase:

    # Проверяем, что метод available_buns возвращает 3 булочки
    def test_available_buns_count(self, db):
        assert len(db.available_buns()) == 3

    # Проверяем, что метод available_ingredients возвращает 6 ингредиентов
    def test_available_ingredients_count(self, db):
        assert len(db.available_ingredients()) == 6

    # Проверяем, что метод available_buns возвращает список булочек
    def test_available_buns_return_type(self, db):
        buns = db.available_buns()
        assert Helpers.check_list_of_type(buns, Bun)

    # Проверяем, что метод available_ingredients возвращает список ингредиентов
    def test_available_ingredients_return_type(self, db):
        ingredients = db.available_ingredients()
        assert Helpers.check_list_of_type(ingredients, Ingredient)
