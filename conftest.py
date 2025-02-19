import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.database import Database

@pytest.fixture
def burger():
    # Создает новый экземпляр класса Burger для тестирования.
    return Burger()

@pytest.fixture
def mock_bun():
    # Создает мок-объект булочки с заданным именем.
    bun = Mock(spec=Bun)
    bun.get_name.return_value = "Sesame Bun"
    return bun

@pytest.fixture
def mock_ingredient():
    # Создает мок-объект ингредиента с заданным именем и типом.
    ingredient = Mock(spec=Ingredient)
    ingredient.get_name.return_value = "Space glue"
    ingredient.get_type.return_value = "filling"
    return ingredient

@pytest.fixture
def db():
    return Database()