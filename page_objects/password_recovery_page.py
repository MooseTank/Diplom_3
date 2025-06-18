import allure
from helpers import *
from page_objects.base_page import BasePage
from locators.password_recovery_locators import PasswordRecoveryLocators


class PasswordRecoveryPage(BasePage):
    @allure.step('Открыть страницу восстановления партоля')
    def password_recovery_page_open(self):
        self.wait_visibility_of_element(PasswordRecoveryLocators.button_forgot_password)
        self.click_on_element(PasswordRecoveryLocators.button_forgot_password)

    @allure.step('Проверить отображение поля email')
    def check_email_input_displaying(self):
        return self.check_displaying_of_element(PasswordRecoveryLocators.input_email)

    @allure.step('Ввести email')
    def input_email(self):
        self.wait_visibility_of_element(PasswordRecoveryLocators.input_email)
        email = create_random_email()
        self.send_keys_to_input(PasswordRecoveryLocators.input_email, email)

    @allure.step('Кликнуть по кнопке "Восстановить"')
    def click_recovery_button(self):
        self.wait_visibility_of_element(PasswordRecoveryLocators.button_recover)
        self.click_on_element(PasswordRecoveryLocators.button_recover)

    @allure.step('Проверить отображение поля password')
    def check_password_input_displaying(self):
        self.wait_visibility_of_element(PasswordRecoveryLocators.input_password)
        return self.check_displaying_of_element(PasswordRecoveryLocators.input_password)

    @allure.step('Ввести password')
    def input_password(self):
        self.wait_visibility_of_element(PasswordRecoveryLocators.input_password)
        password = create_random_password()
        self.send_keys_to_input(PasswordRecoveryLocators.input_password, password)

    @allure.step('Кликнуть на глаз в поле ввода пароля')
    def click_on_eye(self):
        self.wait_visibility_of_element(PasswordRecoveryLocators.eye_icon)
        self.click_on_element(PasswordRecoveryLocators.eye_icon)

    @allure.step('Проверить отображение значения поля password')
    def check_password_value_displaying(self):
        return self.check_displaying_of_element(PasswordRecoveryLocators.value_password_is_visible)

    @allure.step('Проверить невидимость значения поля password')
    def check_password_value_not_displaying(self):
        return self.check_displaying_of_element(PasswordRecoveryLocators.value_password_is_invisible)