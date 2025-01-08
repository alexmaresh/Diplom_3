from selenium.webdriver.common.by import By


class OrdersFeedPageLocators:

    constructor_button = (By.XPATH, "//p[text()='Конструктор']")
    lk_button = (By.XPATH, "//p[text()='Личный Кабинет']")


    last_order = (By.XPATH, "//li[contains(@class,'OrderHistory_listItem__2x95r')][1]")
    order_num_feed = (
        By.XPATH, "//a[@class='OrderHistory_link__1iNby'][1]//p[contains(text(), 'Сегодня')]/preceding-sibling::p")
    in_progress_order = (By.CSS_SELECTOR, "ul.OrderFeed_orderListReady__1YFem li.text_type_digits-default")

    info_modal = (By.XPATH, "//div[contains(@class, 'Modal_orderBox__1xWdi')]")

    all_orders_counter = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    today_orders_counter = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
