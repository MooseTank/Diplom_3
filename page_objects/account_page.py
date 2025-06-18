import allure
from page_objects.base_page import BasePage
from locators.account_page_locators import AccountPageLocators


class AccountPage(BasePage):
    @allure.step('Кликнуть "История заказов"')
    def click_button_order_history(self):
        self.click_on_element(AccountPageLocators.order_history)

    @allure.step('Кликнуть "Вsйти"')
    def click_button_logout(self):
        self.click_on_element(AccountPageLocators.logout_button)

    @allure.step('Дождаться текста описания раздела')
    def wait_visibility_of_description(self):
        self.wait_visibility_of_element(AccountPageLocators.section_description)

    @allure.step('Проверить отображение описания раздела')
    def check_description_displaying(self):
        return self.check_displaying_of_element(AccountPageLocators.section_description)

    @allure.step('Дождаться загрузки кнопки "Зарегистрироваться"')
    def wait_button_register_visibility(self):
        self.wait_visibility_of_element(AccountPageLocators.register_button)

    @allure.step('Проверить отображение "Зарегистрироваться"')
    def check_visibility_of_register_button(self):
        return self.check_displaying_of_element(AccountPageLocators.register_button)