import pytest
from helpers.user_data import BunData  # Импортируем BunData
from praktikum.ingredient import Ingredient  # Импортируем класс Ingredient

class TestIngredient:

    @pytest.mark.parametrize("ingredient", BunData.ingredients)  # Проверяем, что объект Ingredient инициализируется правильно
    def test_ingredient_initialization_creates_correct_object(self, ingredient):
        ing = Ingredient(ingredient["type"], ingredient["name"], ingredient["price"])
        assert ing.get_type() == ingredient["type"]
        assert ing.get_name() == ingredient["name"]
        assert ing.get_price() == ingredient["price"]

    @pytest.mark.parametrize("ingredient", BunData.ingredients)
    def test_ingredient_get_price_returns_correct_value(self, ingredient): # Проверяем метод get_price
        ing = Ingredient(ingredient["type"], ingredient["name"], ingredient["price"])
        assert ing.get_price() == ingredient["price"]

    @pytest.mark.parametrize("ingredient", BunData.ingredients)
    def test_ingredient_get_name_returns_correct_value(self, ingredient): # Проверяем метод get_name
        ing = Ingredient(ingredient["type"], ingredient["name"], ingredient["price"])
        assert ing.get_name() == ingredient["name"]

    @pytest.mark.parametrize("ingredient", BunData.ingredients)
    def test_ingredient_get_type_returns_correct_value(self, ingredient):  # Проверяем метод get_type
        ing = Ingredient(ingredient["type"], ingredient["name"], ingredient["price"])
        assert ing.get_type() == ingredient["type"]
