from faker import Faker
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
            "name": fake.first_name(),
        }
        return payload

    @allure.step("Cоздание пользователя")
    def create_user(self):
        try:
            params = self.generate_user_data()
            resp = requests.post(BR.register, json=params)
            params['accessToken'] = resp.json()['accessToken']
            return params
        except Exception as e:
            print(f"An error occurred: {e}")

    @allure.step("Удаление пользователя")
    def delete_user(self, access_token):
        try:
            resp = requests.delete(BR.user, headers={"Authorization": access_token})
            resp.raise_for_status()
        except Exception as e:
            print(f"An error occurred: {e}")
