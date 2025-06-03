import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import allure


@pytest.fixture
def driver():
    with ((allure.step("Инициализация браузера и его настройка"))):
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        browser.implicitly_wait(20)
        browser.maximize_window()

    yield browser

    with allure.step("Закрытие браузера после теста"):
        browser.quit()


@pytest.fixture
def client(driver):  # используем фикстуру driver
    with allure.step("Переход на страницу и закрытие всплывающего меню"):
        driver.get("https://market-delivery.yandex.ru/moscow?shippingType=delivery")

    with allure.step("Закрытие выпадающего меню, кликом в пустоту"):
        ActionChains(driver).move_by_offset(10, 10).click().perform()

    return driver  # возвращаем готовый к работе драйвер