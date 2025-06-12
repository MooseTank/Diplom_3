from .conftest import *
from page_objects.main_page import MainPage
from page_objects.feed_page import FeedPage
from page_objects.account_page import AccountPage
from page_objects.order_history_page import OdrerHistoryPage


class TestFeedPage:

    @allure.title('Проверка открытия всплывающего окна при клике на заказ')
    def test_displaying_order_details(self, driver):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        main_page.click_feed_button_in_header()
        feed_page.click_on_order_card()
        assert 'бургер' in feed_page.get_text_on_title_orders()

    @allure.title('Проверка отображения из истории пользователя в ленте')
    def test_displaying_in_feed_order_from_history(self, driver, create_user_and_order_with_delete_user, set_user_tokens):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)
        order_history_page = OdrerHistoryPage(driver)
        feed_page = FeedPage(driver)
        main_page.click_personal_account_in_header()
        account_page.click_button_order_history()
        order_id = order_history_page.get_id_of_order_card()
        main_page.click_feed_button_in_header()
        assert feed_page.check_id_order_in_feed(order_id)

    @allure.title('Проверка увеличения счетчика "Выполнено за всё время" при создании нового заказа')
    def test_change_of_quantity_of_orders(self, driver, set_user_tokens):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        main_page.click_feed_button_in_header()
        orders_count_1 = feed_page.get_quantity_of_orders()
        main_page.click_constructor_button()
        main_page.click_login_button_on_main()
        main_page.drag_and_drop_ingredient_to_order()
        main_page.click_make_order_button()
        main_page.main_page_loading_wait()
        main_page.click_close_button_of_conformation()
        main_page.click_feed_button_in_header()
        main_page.main_page_loading_wait()
        orders_count_2 = feed_page.get_quantity_of_orders()
        assert orders_count_1 < orders_count_2

    @allure.title('Проверка увеличения счетчика "Выполнено за сегодня" при создании нового заказа')
    def test_change_of_quantity_of_daily_orders(self, driver, set_user_tokens):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        main_page.click_feed_button_in_header()
        orders_count_1 = feed_page.get_quantity_of_orders_daily()
        main_page.click_constructor_button()
        main_page.click_login_button_on_main()
        main_page.drag_and_drop_ingredient_to_order()
        main_page.click_make_order_button()
        main_page.main_page_loading_wait()
        main_page.click_close_button_of_conformation()
        main_page.click_feed_button_in_header()
        main_page.main_page_loading_wait()
        orders_count_2 = feed_page.get_quantity_of_orders_daily()
        assert orders_count_1 < orders_count_2

    @allure.title('Проверка появления номера заказа в разделе "В работе" после оформления заказа')
    def test_displaying_new_order_in_progress_feed_success(self, driver, set_user_tokens):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        main_page.click_login_button_on_main()
        main_page.drag_and_drop_ingredient_to_order()
        main_page.click_make_order_button()
        main_page.main_page_loading_wait()
        new_order_id = main_page.get_number_of_order_in_conformation()
        main_page.click_close_button_of_conformation()
        main_page.click_feed_button_in_header()
        main_page.main_page_loading_wait()
        assert feed_page.get_order_number_in_feed_progress_section() == '0' + new_order_id