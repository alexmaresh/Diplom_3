from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.account_page import AccountPage
import allure

@allure.feature("Проверка раздела Личный кабинет")
class TestPersonalAccount:

    @allure.title('Проверка перехода на страницу авторизации по клику на Личный кабинет')
    def test_lk_button_redirect(self, driver):
        home_page = HomePage(driver)
        home_page.click_lk_button()
        login_page = LoginPage(driver)
        login_page.check_current_url()

    @allure.title('Проверка перехода в раздел История заказов по клику на кнопку История заказов')
    def test_redirect_to_orders_history(self, driver, created_user):
        home_page = HomePage(driver)
        home_page.click_lk_button()
        login_page = LoginPage(driver)
        login_page.input_email(created_user['email'])
        login_page.input_password(created_user['password'])
        login_page.click_login_submit_button()
        home_page.wait_home_page_loading()
        home_page.click_lk_button()
        account_page = AccountPage(driver)
        account_page.click_orders_history_button()
        account_page.check_current_url()

    @allure.title('Проверка выхода юзера из аккаунта')
    def test_logout(self, driver, created_user):
        home_page = HomePage(driver)
        home_page.click_lk_button()
        login_page = LoginPage(driver)
        login_page.input_email(created_user['email'])
        login_page.input_password(created_user['password'])
        login_page.click_login_submit_button()
        home_page.wait_home_page_loading()
        home_page.click_lk_button()
        account_page = AccountPage(driver)
        account_page.click_logout_button()
        account_page.wait_redirect()
        login_page.check_current_url()
