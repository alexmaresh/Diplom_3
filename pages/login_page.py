from locators.login_page_locators import LoginPageLocators as locs
from pages.base_page import BasePage
from utils.routes import BurgerRoutes as BR
import allure



class LoginPage(BasePage):
    @allure.step('Ввод email в качестве логина пользователя на странице авторизации')
    def input_email(self, email):
        input_email = self.wait_and_find_element(locs.login_email)
        input_email.send_keys(email)

    @allure.step('Ввод пароля пользователя на странице авторизации')
    def input_password(self, password):
        input_password = self.wait_and_find_element(locs.login_password)
        input_password.send_keys(password)

    @allure.step('Клик на кнопку "Войти" на странице авторизации')
    def click_login_submit_button(self):
        login_submit_button = self.wait_and_find_element(locs.login_submit_button)
        login_submit_button.click()

    @allure.step('Клик на ссылку "Восстановить пароль" на странице авторизации')
    def click_recovery_password_link(self):
        recovery_password_link = self.wait_and_find_element(locs.password_recovery_button)
        recovery_password_link.click()

    @allure.step('Проверка: текущая страница это страница авторизации')
    def check_current_url(self):
        current_url = self.get_current_url()
        assert current_url == BR.login
