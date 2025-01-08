import allure
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.password_recovery_page import PasswordRecoveryPage
from pages.password_reset_page import PasswordResetPage


@allure.feature("Проверка раздела Восстановление пароля")
class TestPasswordRecovery:
    @allure.title(
        "Переход на страницу восстановления пароля по кнопке «Восстановить пароль»"
    )
    def test_password_recovery_redirect_link(self, driver):
        home_page = HomePage(driver)
        home_page.click_lk_button()
        login_page = LoginPage(driver)
        login_page.click_recovery_password_link()
        pass_recovery_page = PasswordRecoveryPage(driver)
        pass_recovery_page.check_current_url()

    @allure.title("Ввод почты и клик по кнопке «Восстановить»")
    @allure.description(
        'После ввода email и клика на кнопку "Восстановить", происходит редирект на страницу сброса пароля'
    )
    def test_input_email_and_click_recovery_button(self, driver, created_user):
        home_page = HomePage(driver)
        home_page.click_lk_button()
        login_page = LoginPage(driver)
        login_page.click_recovery_password_link()
        pass_recovery_page = PasswordRecoveryPage(driver)
        pass_recovery_page.input_email(created_user["email"])
        pass_recovery_page.click_recovery_button()
        pass_recovery_page.wait_redirect()
        pass_reset_page = PasswordResetPage(driver)
        pass_reset_page.check_current_url()

    @allure.title("Клик по кнопке показать/скрыть пароль делает поле Пароль активным")
    def test_click_show_hide_button_is_activated_field(self, driver, created_user):
        home_page = HomePage(driver)
        home_page.click_lk_button()
        login_page = LoginPage(driver)
        login_page.click_recovery_password_link()
        pass_recovery_page = PasswordRecoveryPage(driver)
        pass_recovery_page.input_email(created_user["email"])
        pass_recovery_page.click_recovery_button()
        pass_reset_page = PasswordResetPage(driver)
        pass_reset_page.click_show_hide_button()
        pass_reset_page.check_reset_password_field_is_active()

