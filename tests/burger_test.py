from unittest.mock import Mock
from praktikum.ingredient import Ingredient

def test_set_buns_sets_correct_bun_in_burger(burger, mock_bun):
    # Проверяет, что булочка устанавливается правильно в бургер.
    burger.set_buns(mock_bun)
    assert burger.bun == mock_bun

def test_add_ingredient_adds_correct_ingredient_to_burger(burger, mock_ingredient):
    # Проверяет, что ингредиент добавляется в бургер.
    burger.add_ingredient(mock_ingredient)
    assert mock_ingredient in burger.ingredients

def test_remove_ingredient_removes_correct_ingredient_from_burger(burger, mock_ingredient):
    # Проверяет, что ингредиент удаляется из бургера по индексу.
    burger.add_ingredient(mock_ingredient)
    burger.remove_ingredient(0)
    assert mock_ingredient not in burger.ingredients

def test_move_ingredient_moves_ingredient_within_burger(burger):
    # Проверяет, что ингредиент перемещается внутри бургера.
    ingredient1 = Mock(spec=Ingredient)
    ingredient2 = Mock(spec=Ingredient)
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    burger.move_ingredient(0, 1)
    assert burger.ingredients[1] == ingredient1
    assert burger.ingredients[0] == ingredient2

def test_get_price_calculates_correct_price_of_burger(burger, mock_bun, mock_ingredient):
    # Проверяет, что цена бургера рассчитывается правильно.
    mock_bun.get_price.return_value = 2.0
    mock_ingredient.get_price.return_value = 1.0
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient)
    assert burger.get_price() == 5.0

def test_get_receipt_returns_correct_receipt_format(burger, mock_bun, mock_ingredient):
    # Проверяет, что чек бургера формируется правильно.
    mock_bun.get_price.return_value = 2.0
    mock_ingredient.get_price.return_value = 1.0
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient)

    expected_receipt = (
        "(==== Sesame Bun ====)\n"
        "= filling Space glue =\n"
        "(==== Sesame Bun ====)\n"
        "\nPrice: 5.0"
    )
    assert burger.get_receipt() == expected_receipt