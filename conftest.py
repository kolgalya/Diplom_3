import pytest
import random
import string
import allure
import requests
from selenium import webdriver

@allure.step('Открытие браузера в полноэкранном режиме')
@pytest.fixture(params=['Chrome','Firefox']) #'Chrome','Firefox'
def driver(request):
    browser = None
    if request.param == 'Chrome':
        browser = webdriver.Chrome()
    elif request.param == 'Firefox':
        browser = webdriver.Firefox()
    browser.maximize_window()
    yield browser
    browser.quit()

@allure.step('Генерируем случайную строку')
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

@allure.step('Создание пользователя и удаление его после теста')
@pytest.fixture
def create_user():
    email = generate_random_string(5) + '@mail.ru'
    password = generate_random_string(6)
    name = generate_random_string(5)
    user_data = {
        "email": email,
        "password": password,
        "name": name
    }
    user = requests.post('https://stellarburgers.nomoreparties.site/api/auth/register', json=user_data)  # Создание пользователя
    yield user, user_data
    delete = requests.delete('https://stellarburgers.nomoreparties.site/api/auth/user', headers ={"Authorization":user.json()['accessToken']}) # Удаление пользователя