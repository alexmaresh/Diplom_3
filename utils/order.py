import random
import allure
import requests
from utils.routes import BurgerRoutes as BR


class Order:
    @staticmethod
    @allure.step("Получение списка существующих ингредиентов")
    def get_ingredients_dict():
        ingrs = requests.get(BR.ingrs).json()
        if ingrs.get("success"):
            data_list = ingrs.get("data", [])
            result_dict = {item["_id"]: item["name"] for item in data_list}
        else:
            result_dict = {}
        return result_dict

    @allure.step("Создание заказа")
    def create_order(self, access_token):
        data = self.get_ingredients_dict()
        random_ids = random.sample(list(data.keys()), 2)
        params = {"ingredients": random_ids}
        resp = requests.post(
            BR.orders, json=params, headers={"Authorization": access_token}
        )
        order_num = resp.json()["order"]["number"]
        return order_num
