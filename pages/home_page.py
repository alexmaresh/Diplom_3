from locators.home_page_locators import HomePageLocators as locs
from pages.base_page import BasePage
from utils.routes import BurgerRoutes as BR
import allure


class HomePage(BasePage):
    @allure.step("Ожидание полной загрузки главной страницы")
    def wait_home_page_loading(self):
        self.wait_element_loading(locs.main_title)

    @allure.step("Клик на кнопку Личный кабинет в правом верхнем углу главной страницы")
    def click_lk_button(self):
        lk_button = self.wait_and_find_element(locs.lk_button)
        self.click_element(lk_button)

    @allure.step("Клик на кнопку Лента заказов")
    def click_order_feed_button(self):
        order_feed_button = self.wait_and_find_element(locs.order_feed_button)
        self.click_element(order_feed_button)

    @allure.step("Клик на ингредиент в разделе Конструктор")
    def click_ingredient(self):
        ingredient = self.wait_and_find_element(locs.ingredient)
        self.click_element(ingredient)

    @allure.step("Клик на кнопку закрытия всплывающего окна с деталями ингредиента")
    def click_window_with_detail_close_button(self):
        close_button = self.wait_and_find_element(locs.window_close_button)
        close_button.click()

    @allure.step("Клик на кнопку Оформить заказ")
    def click_order_button(self):
        order_button = self.wait_and_find_element(locs.make_order_button)
        self.click_element(order_button)

    @allure.step("Клик на кнопку закрытия окна заказа")
    def click_window_order_close_button(self):
        close_button = self.wait_and_find_element(locs.window_order_close_button)
        self.click_element(close_button)

    @allure.step("Добавить ингредиент в корзину")
    def add_ingredient_to_cart(self):
        source_element = self.wait_and_find_element(locs.ingredient)
        target_element = self.wait_and_find_element(locs.constructor_cart)
        self.drag_and_drop_element(source_element, target_element)

    @allure.step("Проверка: текущая страница это главная страница")
    def check_current_url(self):
        current_url = self.get_current_url()
        assert current_url == BR.base_url

    @allure.step("Всплывающее окно с деталями ингредиента появилось")
    def check_ingredient_detail_window_show(self):
        title = self.wait_and_find_element(locs.modal_details_ingr)
        assert title.is_displayed()

    @allure.step("Всплывающее окно с деталями ингредиента закрылось")
    def check_ingredient_detail_window_close(self):
        title = self.wait_element_invisible(locs.modal_details_ingr)
        assert not title.is_displayed()

    @allure.step("Всплывающее окно с информацией о заказе появилось")
    def check_order_window(self):
        title = self.wait_and_find_element(locs.window_order_title)
        num = self.wait_and_find_element(locs.window_order_number)
        assert title.is_displayed() and num.text is not None

    @allure.step("Счетчик ингредиентов после добавления ингра увеличился")
    def check_counter_increased(self):
        counter = self.wait_and_find_element(locs.ingredient_counter)
        assert int(counter.text) > 0
