import pytest
from selenium import webdriver
from utils.user import User
from utils.order import Order
from utils.routes import BurgerRoutes as BR


@pytest.fixture(params=["firefox", "chrome"])
def driver(request):
    browser = None

    if request.param == "firefox":
        browser = webdriver.Firefox()
    elif request.param == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("start-maximized")
        browser = webdriver.Chrome(options=chrome_options)

    browser.get(BR.base_url)

    yield browser

    browser.quit()


@pytest.fixture(scope="function")
def created_user():
    user = User()
    created_user = user.create_user()
    access_token = created_user['accessToken']
    yield created_user
    user.delete_user(access_token)


@pytest.fixture(scope="function")
def created_order(created_user):
    access_token = created_user['accessToken']
    order = Order()
    order_number = order.create_order(access_token)
    order_params = {
        "order_number": order_number,
        "user_email": created_user['email'],
        "user_password": created_user['password'],
    }

    return order_params
