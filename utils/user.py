from faker import Faker
import random
import allure
import requests
from utils.routes import BurgerRoutes as BR


class User:
    @staticmethod
    @allure.step("Генерация данных юзера")
    def generate_user_data():
        fake = Faker()
        payload = {
            "email": fake.email(),
            "password": fake.password(),
            "name": fake.first_name()
        }
        return payload

    @allure.step("Cоздание пользователя")
    def create_user(self):
        params = self.generate_user_data()
        resp = requests.post(BR.register, json=params)
        return params, resp.json()

    @allure.step("Удаление пользователя")
    def delete_user(self, access_token):
        return requests.delete(BR.user, headers={'Authorization': access_token})

