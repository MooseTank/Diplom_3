import pytest
import allure
from selenium import webdriver
from urls import URLS
from helpers import *
from data import INGREDIENTS
import requests


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
        driver.get(URLS.BASE_URL)
    elif request.param == "firefox":
        driver = webdriver.Firefox()
        driver.set_window_size(1920, 1080)
        driver.get(URLS.BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture
def generate_user_credentials():
    email = create_random_email()
    password = create_random_password()
    name = create_random_name()
    return email, password, name

@pytest.fixture
@allure.title('Фикстура для создания пользователя с рандомными данными и удаления после теста')
def create_and_delete_new_user():
    payload = {
        'email': create_random_email(),
        'password': create_random_password(),
        'name': create_random_name()}
    response = requests.post(URLS.USER_REGISTER, data=payload)
    response_body = response.json()

    yield payload, response_body

    access_token = response_body['accessToken']
    requests.delete(URLS.USER_DELETE, headers={'Authorization': access_token})

@pytest.fixture
@allure.title('Фикстура создания пользователя и заказа пользователя')
def create_user_and_order_with_delete_user(create_and_delete_new_user):
    access_token = create_and_delete_new_user[1]['accessToken']
    headers = {'Authorization': access_token}
    payload = {'ingredients': INGREDIENTS}
    response_body = requests.post(URLS.ORDER_CREATE, data=payload, headers=headers)

    yield access_token, response_body
    requests.delete(URLS.USER_DELETE, headers={'Authorization': access_token})

@pytest.fixture
@allure.title('Фикстура для передачи в драйвер токены созданного пользователя')
def set_user_tokens(driver, create_and_delete_new_user):
    driver.get(URLS.BASE_URL)
    user_data = create_and_delete_new_user[1]
    access_token = user_data.get('accessToken')
    refresh_token = user_data.get('refreshToken')
    driver.execute_script(f'window.localStorage.setItem("accessToken", "{access_token}");')
    driver.execute_script(f'window.localStorage.setItem("refreshToken", "{refresh_token}");')