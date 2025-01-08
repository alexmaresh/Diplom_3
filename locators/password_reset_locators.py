from selenium.webdriver.common.by import By

class PasswordResetLocators:

    show_hide_pass_button = (By.XPATH, "//div[@class='input__icon input__icon-action']")
    pass_field = (By.XPATH, "//div[@class='input__icon input__icon-action']/parent::div")
