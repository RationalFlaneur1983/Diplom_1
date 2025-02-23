from praktikum.bun import Bun
from helpers.user_data import BunData

class TestBun:

    def test_get_name_returns_correct_name(self):
        # Проверяем, что метод get_name возвращает правильное имя.
        bun_data = BunData.buns[0]
        bun = Bun(bun_data["name"], bun_data["price"])
        assert bun.get_name() == bun_data["name"]

    def test_get_price_returns_correct_price(self):
        # Проверяем, что метод get_price возвращает правильную цену.
        bun_data = BunData.buns[1]
        bun = Bun(bun_data["name"], bun_data["price"])
        assert bun.get_price() == bun_data["price"]

    def test_name_change_updates_name_correctly(self):
        # Проверяем, что имя булки можно изменить.
        bun_data = BunData.buns[2]
        bun = Bun(bun_data["name"], bun_data["price"])
        bun.name = "Булка с цельнозерновой мукой"
        assert bun.get_name() == "Булка с цельнозерновой мукой"

    def test_price_change_updates_price_correctly(self):
        # Проверяем, что цену булки можно изменить.
        bun_data = BunData.buns[0]
        bun = Bun(bun_data["name"], bun_data["price"])
        bun.price = 15.00
        assert bun.get_price() == 15.00