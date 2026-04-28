import pytest
import requests
import allure
from selenium import webdriver
from helpers.urls import Url
from pages.base_page import BasePage
from locators.base_locators import BaseLocators
from helpers.data_faker import generate_user, delete_user


def pytest_addoption(parser): # выбор браузера, по умолчанию chrome
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture
def browser(request): # запуск браузера Chrome или Firefox
    browser_name = request.config.getoption("--browser")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Браузер {browser_name} не поддерживается")
    driver.maximize_window()
    yield driver
    driver.quit()

 
@pytest.fixture
def created_user(): # cоздание пользователя через API
    user_data = generate_user(password_length=6)
    with allure.step("Создание тестового пользователя"):
        response = requests.post(f'{Url.CREATE_USER}', json=user_data)
    
        created_user = response.json()
        created_user['id'] = created_user.get('id')
        created_user['email'] = user_data['email']  
        created_user['password'] = user_data['password']  

    yield created_user
    token = created_user.get("accessToken")
    if token:
        with allure.step("Удаление тестового пользователя"):
            delete_response = delete_user(token)
            allure.attach(
                f"Статус удаления: {delete_response.status_code}\n"
                f"Тело ответа: {delete_response.text}",
                name="Результат удаления пользователя",
                attachment_type=allure.attachment_type.TEXT
            )


@pytest.fixture 
def logged_in_browser(browser, created_user): # авторизация пользователя через UI
    browser.get(Url.BASE_URL)
    base_page = BasePage(browser)
    base_page._click_outside_modal()
    base_page.login(created_user["email"], created_user["password"])
    base_page.wait_for_element_visible(BaseLocators.INGREDIENT_BUN)
    return browser
