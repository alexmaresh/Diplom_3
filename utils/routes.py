class BurgerRoutes:
    base_url: str = "https://stellarburgers.nomoreparties.site/"
    login: str = base_url + "login"
    forget_password: str = base_url + "forgot-password"
    reset_password: str = base_url + "reset-password"
    account: str = base_url + "account/profile"
    order_history: str = base_url + "account/order-history"
    order_feed: str = base_url + "feed"

    # API
    api_url: str = base_url + "api/"
    register: str = api_url + "auth/register"
    user: str = api_url + "auth/user"
    ingrs: str = api_url + "ingredients"
    orders: str = api_url + "orders"
