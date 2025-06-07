from selenium.webdriver.common.by import By


class AccountPageLocators:
    profile = (By.XPATH, '//a[@href = "/account/profile]')
    order_history = (By.XPATH, '//a[@href = "/account/order-history"]')
    logout_button = (By.XPATH, '//button[@type = "button"]')
    register_button = (By.XPATH, '//a[text() = "Зарегистрироваться"]')
    section_description = (By.XPATH, '//p[contains(@class, "Account_text")]')