import allure
from pages.base_page import BasePage
from utils.routes import BurgerRoutes as BR

from locators.password_recovery_locators import PasswordRecoveryLocators as locs


class PasswordRecoveryPage(BasePage):
    @allure.step('Ввод email на странице восстановления пароля')
    def input_email(self, email):
        input_email = self.wait_and_find_element(locs.recovery_email_field)
        input_email.send_keys(email)

    @allure.step('Клик на кнопку "Восстановить" на странице восстановления пароля')
    def click_recovery_button(self):
        login_submit_button = self.wait_and_find_element(locs.recovery_button)
        login_submit_button.click()

    @allure.step('Проверка: текущая страница это страница восстановления пароля')
    def check_current_url(self):
        current_url = self.get_current_url()
        assert current_url == BR.forget_password