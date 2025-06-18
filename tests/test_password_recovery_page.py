import allure
from page_objects.main_page import MainPage
from page_objects.password_recovery_page import PasswordRecoveryPage


class TestPasswordRecoveryPage:
    @allure.title('Проверка перехода на страницу восстановления пароля')
    def test_transfer_to_recovery_password_page(self, driver):
        main_page = MainPage(driver)
        main_page.click_login_button_on_main()
        recovery_page = PasswordRecoveryPage(driver)
        recovery_page.password_recovery_page_open()
        assert recovery_page.check_email_input_displaying()

    @allure.title('Проверка перехода к восстановлению пароля при вводе почты и нажатии кнопки "Восстановить"')
    def test_click_recovery_button(self, driver):
        main_page = MainPage(driver)
        main_page.click_login_button_on_main()
        recovery_page = PasswordRecoveryPage(driver)
        recovery_page.password_recovery_page_open()
        recovery_page.input_email()
        recovery_page.click_recovery_button()
        assert recovery_page.check_email_input_displaying()

    @allure.title('Проверка отображения введенных символов после нажатия кнопки "показать/скрыть пароль"')
    def test_click_on_eye_makes_password_visible(self, driver):
        main_page = MainPage(driver)
        main_page.click_login_button_on_main()
        recovery_page = PasswordRecoveryPage(driver)
        recovery_page.password_recovery_page_open()
        recovery_page.input_email()
        recovery_page.click_recovery_button()
        recovery_page.input_password()
        recovery_page.click_on_eye()
        assert recovery_page.check_password_value_displaying()

    @allure.title('Проверка маскировки введенных символов после двух нажатий кнопки "показать/скрыть пароль"')
    def test_double_click_on_eye_makes_password_invisible(self, driver):
        main_page = MainPage(driver)
        main_page.click_login_button_on_main()
        recovery_page = PasswordRecoveryPage(driver)
        recovery_page.password_recovery_page_open()
        recovery_page.input_email()
        recovery_page.click_recovery_button()
        recovery_page.input_password()
        recovery_page.click_on_eye()
        recovery_page.click_on_eye()
        assert recovery_page.check_password_value_not_displaying()