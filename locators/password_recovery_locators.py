from selenium.webdriver.common.by import By


class PasswordRecoveryLocators:
    recovery_email_field = (By.XPATH, "//input[@name='name']")
    recovery_button = (By.XPATH, "//button[text()='Восстановить']")
