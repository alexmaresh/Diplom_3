from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.orders_feed_page import OrdersFeedPage
import allure


@allure.feature("Проверка основного функционала")
class TestMainFunctionality:
    @allure.title("Переход на главную по клику на Конструктор")
    def test_constructor_button_redirect_home_page(self, driver):
        home_page = HomePage(driver)
        home_page.click_order_feed_button()
        order_feed_page = OrdersFeedPage(driver)
        order_feed_page.click_constructor_button()
        home_page.check_current_url()

    @allure.title("Переход на Ленту заказов по клику на кнопку Лента заказов")
    def test_order_feed_button_redirect_feed(self, driver):
        home_page = HomePage(driver)
        home_page.click_order_feed_button()
        order_feed_page = OrdersFeedPage(driver)
        order_feed_page.check_current_url()

    @allure.title(
        "Всплывающее окно с деталями об ингре при клике на ингредиент появилось"
    )
    def test_click_ingredient_window(self, driver):
        home_page = HomePage(driver)
        home_page.click_ingredient()
        home_page.check_ingredient_detail_window_show()

    @allure.title("Всплывающее окно по клику на крестик закрылось")
    def test_close_window_with_detail(self, driver):
        home_page = HomePage(driver)
        home_page.click_ingredient()
        home_page.click_window_with_detail_close_button()
        home_page.check_ingredient_detail_window_close()

    @allure.title("Увеличился счетчик ингредиента при добавлении ингредиента в заказ")
    def test_add_ingredient_in_order_counter_is_increased(self, driver):
        home_page = HomePage(driver)
        home_page.add_ingredient_to_cart()
        home_page.check_counter_increased()

    @allure.title("Авторизованный юзер может оформить заказ")
    def test_create_order_success(self, driver, created_user):
        home_page = HomePage(driver)
        home_page.click_lk_button()
        login_page = LoginPage(driver)
        login_page.input_email(created_user["email"])
        login_page.input_password(created_user["password"])
        login_page.click_login_submit_button()
        home_page.wait_home_page_loading()
        home_page.add_ingredient_to_cart()
        home_page.click_order_button()
        home_page.check_order_window()
