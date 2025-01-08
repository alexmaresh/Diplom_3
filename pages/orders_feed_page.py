from locators.orders_feed_page_locators import OrdersFeedPageLocators as locs
from pages.base_page import BasePage
from utils.routes import BurgerRoutes as BR
import allure


class OrdersFeedPage(BasePage):
    @allure.step("Клик на кнопку Конструктор")
    def click_constructor_button(self):
        constructor_button = self.wait_and_find_element(locs.constructor_button)
        constructor_button.click()

    @allure.step("Клик на кнопку Личный кабинет")
    def click_lk_button(self):
        lk_button = self.wait_and_find_element(locs.lk_button)
        lk_button.click()

    @allure.step("Клик на последний заказ в разделе Лента заказов")
    def click_order_in_feed(self):
        order = self.wait_and_find_element(locs.last_order)
        order.click()

    @allure.step("Получение номера последнего заказа в разделе Лента заказов")
    def get_last_order_number_from_feed(self):
        order_num = self.wait_and_find_element(locs.order_num_feed)
        return int(order_num.text[2:])

    @allure.step("Получение значения счетчика Выполнено за всё время")
    def get_counter_all_orders(self):
        counter = self.wait_and_find_element(locs.all_orders_counter)
        return int(counter.text)

    @allure.step("Получение значения счетчика Выполнено за сегодня")
    def get_counter_today_orders(self):
        counter = self.wait_and_find_element(locs.today_orders_counter)
        return int(counter.text)

    @allure.step("Получение номера заказа из раздела В работе")
    def get_number_of_order_in_progress(self):
        order_num = self.wait_and_find_element(locs.in_progress_order)
        return int(order_num.text[1:])

    @allure.step("Проверка: текущая страница это страница Ленты заказов")
    def check_current_url(self):
        current_url = self.get_current_url()
        assert current_url == BR.order_feed

    @allure.step("Появление окна с информацией о заказе")
    def check_window_order_info_show(self):
        window = self.wait_and_find_element(locs.info_order_window)

        assert window.is_displayed()

    @allure.step("Номер заказа из Истории заказов есть в Ленте заказов")
    def check_order_number_in_feed(self, order_number_from_history):
        assert self.get_last_order_number_from_feed() == order_number_from_history

    @allure.step("Создание нового заказа увеличивает счётчик Выполнено за всё время")
    def check_counter_all_orders_increased(self, order_count):
        new_order_count = self.get_counter_all_orders()

        assert new_order_count > order_count

    @allure.step("Создание нового заказа увеличивает счётчик Выполнено за сегодня")
    def check_counter_today_orders_increased(self, order_count):
        new_order_count = self.get_counter_today_orders()

        assert new_order_count > order_count

    @allure.step("После оформления номер заказа есть в разделе В работе")
    def check_order_number_in_order_in_progress(self, order_number):
        assert self.get_number_of_order_in_progress() == order_number
