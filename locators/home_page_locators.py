from selenium.webdriver.common.by import By


class HomePageLocators:
    lk_button = (By.XPATH, "//p[text()='Личный Кабинет']")
    order_feed_button = (By.XPATH, "//p[text()='Лента Заказов']")
    make_order_button = (By.XPATH, "//button[text()='Оформить заказ']")
    main_title = (By.XPATH, "//h1")

    ingredient = (
        By.XPATH,
        "//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6')]",
    )
    ingredient_counter = (By.XPATH, "//p[@class='counter_counter__num__3nue1']")
    constructor_cart = (
        By.XPATH,
        "//ul[@class='BurgerConstructor_basket__list__l9dp_']",
    )

    modal_details_ingr = (By.XPATH, "//h2[text()='Детали ингредиента']")
    window_close_button = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal_opened__3ISw4')]//button",
    )

    window_order_title = (By.XPATH, "//p[text()='идентификатор заказа']")
    window_order_number = (
        By.XPATH,
        "//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq')]",
    )
    window_order_close_button = (
        By.XPATH,
        "//button[contains(@class, 'Modal_modal__close_modified__3V5XS')]",
    )
