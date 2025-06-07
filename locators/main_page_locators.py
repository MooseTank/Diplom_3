from selenium.webdriver.common.by import By


class MainPageLocotors:
    login_button_in_main = (By.XPATH, './/button[text() = "Войти в аккаунт"]')
    personal_account_button = (By.XPATH, '//p[text()="Личный Кабинет"]/parent::a')
    make_order_button = (By.XPATH, '//button[text()="Оформить заказ"]')
    constructor_button = (By.XPATH, '//p[text() = "Конструктор"]')
    selected_button = (By.XPATH, ('//div[@class = '
                                  '"tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]'))
    constructor_title = (By.XPATH, '//section[contains(@class, "BurgerIngredients_ingredients")]/h1')
    buns_block = (By.XPATH, '//span[text() = "Булки"]')
    sauces_block = (By.XPATH, '//span[text() = "Соусы"]')
    fillings_block = (By.XPATH, '//span[text() = "Начинки"]')
    button_order_feed_in_header = (By.XPATH, '//p[text()="Лента Заказов"]/parent::a/parent::li')
    ingredient_1 = (By.XPATH, '(.//p[@class="BurgerIngredient_ingredient__text__yp3dH"])[1]')
    header_of_modal_details = (By.XPATH, '//h2[contains(@class, "Modal_modal__title") and contains(text(), "Детали")]')
    button_close_modal = (By.XPATH, '//section[contains(@class, '
                                    '"Modal_modal_opened")]//button[contains(@class, "close")]')
    burger_ingredient = (By.XPATH, './/*[@alt="Флюоресцентная булка R2-D3"]')
    place_for_ingredients = (By.XPATH, '//section[contains(@class, "BurgerConstructor_basket")]')
    content_of_order = (By.CSS_SELECTOR, '.constructor-element_pos_top .constructor-element__row')
    button_make_order = (By.CLASS_NAME, 'button_button__33qZ0')
    count_of_ingredient = (By.XPATH, './/a[@class="BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8"]//p['
                                     '@class="counter_counter__num__3nue1"][1]')
    confirmation_modal_of_order = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]/div[contains'
                                             '(@class, "Modal_modal__container")]')
    number_of_order_in_modal_confirmation = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//h2')
    button_close_confirmation = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")'
                                           ']//button[contains(@class, "close")]')