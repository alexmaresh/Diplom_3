from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.orders_feed_page import OrdersFeedPage
from pages.account_page import AccountPage
import allure


@allure.feature("Проверка раздела Лента заказов")
class TestOrdersFeed:
    @allure.title("При клике на заказ откроется всплывающее окно с деталями заказа")
    def test_click_order_window_show(self, driver):
        home_page = HomePage(driver)
        home_page.click_order_feed_button()
        order_feed_page = OrdersFeedPage(driver)
        order_feed_page.click_order_in_feed()
        order_feed_page.check_window_order_info_show()

    @allure.title(
        "Заказы пользователя из раздела История заказов отображаются на странице Лента заказов"
    )
    def test_user_orders_in_feed(self, driver, created_order):
        home_page = HomePage(driver)
        home_page.click_lk_button()
        login_page = LoginPage(driver)
        login_page.input_email(created_order["user_email"])
        login_page.input_password(created_order["user_password"])
        login_page.click_login_submit_button()
        home_page.wait_home_page_loading()
        home_page.click_lk_button()
        account_page = AccountPage(driver)
        account_page.wait_account_page_loading()
        account_page.click_orders_history_button()
        order_number = account_page.get_order_number_from_history()
        order_feed_page = OrdersFeedPage(driver)
        order_feed_page.check_order_number_in_feed(order_number)

    @allure.title(
        "При создании нового заказа счётчик Выполнено за всё время увеличивается"
    )
    def test_new_order_counter_all_increased(self, driver, created_user):
        home_page = HomePage(driver)
        home_page.click_order_feed_button()
        order_feed_page = OrdersFeedPage(driver)
        order_count = order_feed_page.get_counter_all_orders()
        order_feed_page.click_lk_button()
        login_page = LoginPage(driver)
        login_page.input_email(created_user["email"])
        login_page.input_password(created_user["password"])
        login_page.click_login_submit_button()
        home_page.wait_home_page_loading()
        home_page.move_ingredient_to_order()
        home_page.click_order_button()
        home_page.click_window_order_close_button()
        home_page.wait_home_page_loading()
        home_page.click_order_feed_button()
        order_feed_page.check_counter_all_orders_increased(order_count)

    @allure.title(
        "При создании нового заказа счётчик Выполнено за сегодня увеличивается"
    )
    def test_new_order_counter_today_increased(self, driver, created_user):
        home_page = HomePage(driver)
        home_page.click_order_feed_button()
        order_feed_page = OrdersFeedPage(driver)
        order_count = order_feed_page.get_counter_today_orders()
        order_feed_page.click_lk_button()
        login_page = LoginPage(driver)
        login_page.input_email(created_user["email"])
        login_page.input_password(created_user["password"])
        login_page.click_login_submit_button()
        home_page.wait_home_page_loading()
        home_page.add_ingredient_to_cart()
        home_page.click_order_button()
        home_page.click_window_order_close_button()
        home_page.wait_home_page_loading()
        home_page.click_order_feed_button()
        order_feed_page.check_counter_today_orders_increased(order_count)

    @allure.title("После оформления заказа его номер появляется в разделе В работе")
    def test_user_order_number_in_lst_order_in_work(self, driver, created_order):
        home_page = HomePage(driver)
        home_page.click_order_feed_button()
        order_feed_page = OrdersFeedPage(driver)
        order_number = created_order["order_number"]
        order_feed_page.check_order_number_in_order_in_progress(order_number)
