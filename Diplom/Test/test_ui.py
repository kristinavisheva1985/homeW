import sys
from pathlib import Path
import allure
import pytest
from pages.ui_client import MainPage
from config import SEARCH_QUERY_CORN, SEARCH_QUERY_TOMATOES
from selenium.webdriver.support import expected_conditions as EC

# Добавляем корневую директорию в путь поиска модулей(это нужно)
sys.path.append(str(Path(__file__).parent.parent))


@pytest.mark.api_test
@allure.id("DELIVERY UI")
@allure.feature('Позитивные UI-тесты')
@allure.story('Переход с дочерней страницы Деливери на главную')
def test_search_and_click_ostrich(client):
    page = MainPage(client)
    with allure.step(f"Провести поиск продукта, например кукурузы '{SEARCH_QUERY_CORN}'"):
        assert page.search_product(SEARCH_QUERY_CORN)

    with allure.step("Кликнуть на кнопку поиска и дождаться смены страницы на дочернюю"):
        page.click_search_button()

    with allure.step("Кликнуть на баннер страуса и перейти на главную страницу"):
        page.click_ostrich_banner()


@allure.id("DELIVERY UI")
@allure.feature('Позитивные UI-тесты')
@allure.story('Работа с полем поиска')
def test_search_field(client):
    page = MainPage(client)
    with allure.step(f"Ввести запрос '{SEARCH_QUERY_TOMATOES}' в поле поиска"):
        assert page.search_product(SEARCH_QUERY_TOMATOES)

    with allure.step("Выполнить клик на кнопке поиска"):
        page.click_search_button()


@allure.id("DELIVERY UI")
@allure.feature('Позитивные UI-тесты')
@allure.story('Клик по кнопке "Все" в секции "Магазины"')
def test_click_all_shops_button(client):
    with allure.step("Кликнуть на кнопку 'Все'"):
        button_clicked = MainPage(client).click_all_shops_button()
        assert button_clicked is True, "Кнопка 'Все' не была успешно нажата"


@allure.id("DELIVERY UI")
@allure.feature('Позитивные UI-тесты')
@allure.story("Клик по кнопке 'Укажите адрес доставки'")
def test_click_delivery_address(client):
    page = MainPage(client)
    with allure.step("Кликнуть на кнопку 'Укажите адрес доставки'"):
        page.wait.until(EC.element_to_be_clickable(page.DELIVERY_BUTTON)).click()
        try:
            page.wait.until(EC.element_to_be_clickable(page.WHERE_TO_DELIVER_BTN)).click()
        except:
            pass
        page.wait.until(EC.visibility_of_element_located(page.MODAL_WINDOW))


@allure.id("DELIVERY UI")
@allure.feature('Негативные UI-тесты')
@allure.story('Клики по элементам страницы (Например по баннеру магазина Магнит с отсутствующими данными MAGNIT_BANNER)')
def test_click_magnit_banner(client):
    main_page = MainPage(client)

    with allure.step("Кликнуть на баннер Магнита (данных на него нет)"):
        try:
            main_page.click_magnit_banner()
        except AttributeError:
            return
    assert False, "Локатор MAGNIT_BANNER доступен"