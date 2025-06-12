from .conftest import *
from page_objects.main_page import MainPage
from page_objects.order_history_page import OdrerHistoryPage
from page_objects.account_page import AccountPage


class TestAccountPage:
    @allure.title('Проверка перехода по клику на "Личный кабинет"')
    def test_transfer_to_account_page(self, driver, set_user_tokens):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)
        main_page.click_personal_account_in_header()
        account_page.wait_visibility_of_description()
        assert account_page.check_description_displaying() is True

    @allure.title('Проверка перехода в раздел "История заказов"')
    def test_transfer_to_order_history_page(self, driver, set_user_tokens, create_user_and_order_with_delete_user):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)
        order_history_page = OdrerHistoryPage(driver)
        main_page.click_personal_account_in_header()
        account_page.wait_visibility_of_description()
        account_page.click_button_order_history()
        order_history_page.wait_order_card_visibility()
        assert 'бургер' in order_history_page.get_text_of_order_card_title()

    @allure.title('Проверка выхода из аккаунта')
    def test_profile_logout(self, driver, set_user_tokens):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)
        main_page.click_personal_account_in_header()
        account_page.wait_visibility_of_description()
        account_page.click_button_logout()
        account_page.wait_button_register_visibility()
        assert account_page.check_visibility_of_register_button()