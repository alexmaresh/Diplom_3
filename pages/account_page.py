from pages.base_page import BasePage
from locators.account_page_locators import AccountPageLocators as locs
from utils.routes import BurgerRoutes as BR
import allure


class AccountPage(BasePage):

    @allure.step('Ожидание загрузки страницы ЛК')
    def wait_account_page_loading(self):
        self.wait_element_loading(locs.profile_button)

    @allure.step('Клик на кнопку История заказов в ЛК')
    def click_orders_history_button(self):
        orders_history_link = self.wait_and_find_element(locs.orders_history_link)
        orders_history_link.click()

    @allure.step('Клик на кнопку Выход в ЛК')
    def click_logout_button(self):
        logout_button = self.wait_and_find_element(locs.logout_button)
        self.driver.execute_script("arguments[0].click();", logout_button)

    @allure.step('Получение номера заказа пользователя Истории заказов')
    def get_order_number_from_history(self):
        order_num = self.wait_and_find_element(locs.order_number_from_history)
        return int(order_num.text[2:])

    @allure.step('Проверка: текущая страница это страница История заказов')
    def check_current_url(self):
        current_url = self.get_current_url()
        assert current_url == BR.order_history

    @allure.step('Ожидание редиректа')
    def wait_redirect(self):
        return self.wait_url_change(BR.account)
