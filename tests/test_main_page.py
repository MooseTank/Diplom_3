from .conftest import *
from page_objects.main_page import MainPage
from page_objects.feed_page import FeedPage


class TestMainPage:
    @allure.title('Проверка перехода по клику на "Конструктор"')
    def test_transfer_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.click_feed_button_in_header()
        main_page.click_constructor_button()
        assert 'Соберите бургер' in main_page.get_text_constructor_title()

    @allure.title('Проверка перехода по клику на "Лента заказов"')
    def test_transfer_to_order_history(self, driver):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        main_page.click_feed_button_in_header()
        assert feed_page.get_text_on_title_orders_list() == 'Лента заказов'

    @allure.title('Проверка появления всплывающего окна с деталями ингредиента при клике на ингредиент')
    def test_displaying_window_details_of_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient()
        assert main_page.check_displaying_of_modal_details()

    @allure.title('Проверка закрытия окна "Детали ингредиента" кликом по крестику')
    def test_close_window_details_of_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient()
        main_page.close_modal()
        assert main_page.check_not_displaying_of_modal_details()

    @allure.title('Проверка увеличения каунтера ингредиента при добавлении данного ингредиента')
    def test_changing_counter_of_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.drag_and_drop_ingredient_to_order()
        assert main_page.get_count_of_ingredients() == '2'

    @allure.title('Залогиненый пользователь может оформить заказ')
    def test_authorized_user_make_order(self, driver, set_user_tokens):
        main_page = MainPage(driver)
        main_page.click_login_button_on_main()
        main_page.drag_and_drop_ingredient_to_order()
        main_page.click_make_order_button()
        assert main_page.check_conformation_of_order_is_displaying()