from locators.home_page_locators import HomePageLocators as locs
from pages.base_page import BasePage
from utils.routes import BurgerRoutes as BR
import allure


class HomePage(BasePage):
    @allure.step('Ожидание полной загрузки главной страницы')
    def wait_home_page_loading(self):
        self.wait_element_loading(locs.main_title)

    @allure.step('Клик на кнопку Личный кабинет в правом верхнем углу главной страницы')
    def click_lk_button(self):
        lk_button = self.wait_and_find_element(locs.lk_button)
        self.click_element(lk_button)

    @allure.step('Клик на кнопку Лента Заказов')
    def click_order_feed_button(self):
        order_feed_button = self.wait_and_find_element(locs.order_feed_button)
        self.click_element(order_feed_button)

    @allure.step('Клик на ингредиент в разделе Конструктор')
    def click_ingredient(self):
        ingredient = self.wait_and_find_element(locs.ingredient)
        self.click_element(ingredient)

    @allure.step('Клик на кнопку закрытия всплывающего окна с деталями ингредиента')
    def click_window_with_detail_close_button(self):
        close_button = self.wait_and_find_element(locs.window_close_button)
        close_button.click()

    @allure.step('Клик на кнопку Оформить заказ')
    def click_order_button(self):
        order_button = self.wait_and_find_element(locs.order_button)
        self.click_element(order_button)

    @allure.step('Клик на кнопку закрытия окна оформленного заказа')
    def click_window_order_close_button(self):
        close_button = self.wait_and_find_element(locs.window_order_close_button)
        self.click_element(close_button)

    @allure.step('Перемещение ингредиента в корзину-конструктор')
    def move_ingredient_to_order(self):
        source_element = self.wait_and_find_element(locs.ingredient)
        target_element = self.wait_and_find_element(locs.constructor_basket)
        self.drag_and_drop_element(source_element, target_element)

    @allure.step('Проверка, что текущая страница это главная страница')
    def check_current_url(self):
        current_url = self.get_current_url()
        assert current_url == BR.base_url

    @allure.step('Проверка, что всплывающее окно с деталями ингредиента появляется')
    def check_window_with_ingredient_detail_is_appear(self):
        title = self.wait_and_find_element(locs.modal_details_ingr)
        assert title.is_displayed()

    @allure.step('Проверка, что всплывающее окно с деталями ингредиента закрывается')
    def check_window_with_ingredient_detail_is_disappear(self):
        title = self.wait_element_invisible(locs.home_page_locators.modal_details_ingr)
        assert not title.is_displayed()

    @allure.step('Проверка, что окно с информацией об успешном оформлении заказа появляется')
    def check_order_window_is_appear(self):
        title = self.wait_and_find_element(locators.home_page_locators.window_order_title)
        num = self.wait_and_find_element(locators.home_page_locators.window_order_number)
        assert title.is_displayed() and num.text is not None

    @allure.step('Проверка увеличения показателя счетчика ингредиента после добавления его в корзину-конструктор')
    def check_ingredient_counter_is_increased(self):
        counter = self.wait_and_find_element(locators.home_page_locators.ingredient_counter)
        assert int(counter.text) > 0
