import allure
from page_objects.base_page import BasePage
from locators.order_history_page_locators import OrderHistoryPageLocators


class OdrerHistoryPage(BasePage):
    @allure.step('Дождаться загрузки карточки заказа')
    def wait_order_card_visibility(self):
        self.wait_visibility_of_element(OrderHistoryPageLocators.order_card)

    @allure.step('Получить текст карточки заказа')
    def get_text_of_order_card_title(self):
        return self.get_text_on_element(OrderHistoryPageLocators.order_card_title)

    @allure.step('Получить номер заказа в карточке')
    def get_id_of_order_card(self):
        return self.get_text_on_element(OrderHistoryPageLocators.order_card_id)