from selenium.webdriver.common.by import By


class LoginPageLocators:
    login_email = (By.XPATH, "//input[@name='name']")
    login_password = (By.XPATH, "//input[@name='Пароль']")
    login_submit_button = (By.XPATH, "//Button[text()='Войти']")
    password_recovery_button = (By.XPATH, "//a[text()='Восстановить пароль']")
