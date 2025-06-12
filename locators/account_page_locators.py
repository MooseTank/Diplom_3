from selenium.webdriver.common.by import By


class AccountPageLocators:
    # Профиль
    profile = (By.XPATH, '//a[@href = "/account/profile]')

    # История заказов
    order_history = (By.XPATH, '//a[@href = "/account/order-history"]')

    # Кнопка "Выход"
    logout_button = (By.XPATH, '//button[@type = "button"]')

    # Кнопка "Зарегистрироваться"
    register_button = (By.XPATH, '//a[text() = "Зарегистрироваться"]')

    # Описание раздела
    section_description = (By.XPATH, '//p[contains(@class, "Account_text")]')