from selenium.webdriver.common.by import By

class AccountPageLocators:
    orders_history_link = (By.XPATH, "//a[text()='История заказов']")
    logout_button = (By.XPATH, "//button[text()='Выход']")
    profile_button = (By.XPATH, "//a[text()='Профиль']")
    order_number_from_history = (
        By.XPATH, "//a[@class='OrderHistory_link__1iNby']//p[contains(text(), 'Сегодня')]/preceding-sibling::p")
