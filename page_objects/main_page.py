import allure
from page_objects.base_page import BasePage
from locators.main_page_locators import MainPageLocotors


class MainPage(BasePage):
    @allure.step('Кликнуть по кнопке перехода в личный аккаунт в хэдере')
    def click_personal_account_in_header(self):
        self.wait_visibility_of_element(MainPageLocotors.personal_account_button)
        self.click_on_element(MainPageLocotors.personal_account_button)

    @allure.step('Кликнуть по кнопке "Лента заказов" в хэдере')
    def click_feed_button_in_header(self):
        self.wait_visibility_of_element(MainPageLocotors.button_order_feed_in_header)
        self.click_on_element(MainPageLocotors.button_order_feed_in_header)

    @allure.step('Перейти на страницу "Конструктор"')
    def click_constructor_button(self):
        self.wait_visibility_of_element(MainPageLocotors.constructor_button)
        self.click_on_element(MainPageLocotors.constructor_button)

    @allure.step('Получение заголовка конструктора')
    def get_text_constructor_title(self):
        return self.get_text_on_element(MainPageLocotors.constructor_title)

    @allure.step('Клик по кнопке "Войти в аккаунт" на главной')
    def click_login_button_on_main(self):
        self.click_on_element(MainPageLocotors.login_button_in_main)

    @allure.step('Проверка отображение окна о создании заказа')
    def check_conformation_of_order_is_displaying(self):
        self.wait_visibility_of_element(MainPageLocotors.confirmation_modal_of_order)
        return self.check_displaying_of_element(MainPageLocotors.confirmation_modal_of_order)

    @allure.step('Кликнуть по ингредиенту')
    def click_on_ingredient(self):
        self.wait_visibility_of_element(MainPageLocotors.ingredient_1)
        self.click_on_element(MainPageLocotors.ingredient_1)

    @allure.step('Проверка отображения окна "Детали ингредиента"')
    def check_displaying_of_modal_details(self):
        self.wait_visibility_of_element(MainPageLocotors.header_of_modal_details)
        return self.check_displaying_of_element(MainPageLocotors.header_of_modal_details)

    @allure.step('Проверка отсутствия отображения окна "Детали ингредиента"')
    def check_not_displaying_of_modal_details(self):
        self.wait_for_closing_of_element(MainPageLocotors.header_of_modal_details)
        if not self.check_displaying_of_element(MainPageLocotors.header_of_modal_details):
            return True

    @allure.step('Закрыть окно "Детали ингредиента"')
    def close_modal(self):
        self.wait_visibility_of_element(MainPageLocotors.button_close_modal)
        self.click_on_element(MainPageLocotors.button_close_modal)


    @allure.step('Добавить ингредиенты')
    def drag_and_drop_ingredient_to_order(self):
        source_element = self.find_element_with_wait(MainPageLocotors.burger_ingredient)
        target_element = self.find_element_with_wait(MainPageLocotors.place_for_ingredients)
        self.drag_and_drop_element(source_element, target_element)

    @allure.step('Получение количества ингредиентов')
    def get_count_of_ingredients(self):
        return self.get_text_on_element(MainPageLocotors.count_of_ingredient)

    @allure.step('Кликнуть на кнопку создания заказа')
    def click_make_order_button(self):
        self.click_on_element(MainPageLocotors.make_order_button)

    @allure.step('Проверка отображения окна о создании заказа')
    def check_displaying_confirmation_of_order(self):
        return self.check_displaying_of_element(MainPageLocotors.confirmation_modal_of_order)
    @allure.step('Получение номера в окне о создании заказа')
    def get_number_of_order_in_conformation(self):
        self.wait_for_element_to_change_text(MainPageLocotors.number_of_order_in_modal_confirmation, '9999')

    @allure.step('Кликнуть по кнопке закрытия окна о создании заказа')
    def click_close_button_of_conformation(self):
        self.check_element_is_clickable(MainPageLocotors.button_close_confirmation)
        self.click_on_element(MainPageLocotors.button_close_confirmation)