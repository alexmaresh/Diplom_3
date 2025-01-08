import allure
from pages.base_page import BasePage
from utils.routes import BurgerRoutes as BR
from locators.password_reset_locators import PasswordResetLocators as locs


class PasswordResetPage(BasePage):
    @allure.step("Клик на кнопку Показать/скрыть пароль в поле ввода пароля")
    def click_show_hide_button(self):
        submit_button = self.wait_and_find_element(locs.show_hide_pass_button)
        submit_button.click()

    @allure.step(
        "Проверка, что клик на кнопку Показать/скрыть пароль делает поле ввода пароля активным"
    )
    def check_reset_password_field_is_active(self):
        pass_field = self.wait_and_find_element(locs.pass_field)
        assert "input_status_active" in pass_field.get_attribute("class")

    @allure.step("Проверка: текущая страница это страница cброса пароля")
    def check_current_url(self):
        current_url = self.get_current_url()
        assert current_url == BR.reset_password, current_url
