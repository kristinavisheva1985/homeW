import allure
import pytest
from selenium import webdriver
from login_page import LoginPage
from main_page import MainPage
from cart_page import CartPage
from checkout_page import CheckoutPage


@pytest.fixture
def browser():
    """
    Фикстура PyTest, открывающая и закрывающая браузер Chrome для выполнения тестов.

    :yield: Объект браузера (Selenium WebDriver).
    """
    with allure.step("Открытие браузера"):
        driver = webdriver.Chrome()
        yield driver
    with allure.step("Закрытие браузера"):
        driver.quit()


@allure.epic("Магазин")
@allure.title("Тестирование магазина")
@allure.severity("blocker")  # Критический уровень важности
@allure.feature("Тестирование процесса покупки")
@allure.story("Полный поток покупки товаров")
def test_shopping_flow(browser):
    """
    Полностью автоматизированный тест полного цикла покупки товаров в магазине.

    Шаги теста:
    1. Авторизация пользователя.
    2. Добавление выбранных товаров в корзину.
    3. Оформление заказа и заполнение контактных данных.
    4. Подтверждение итоговой суммы заказа.

    :param browser: Объект браузера, созданный фикстурой.
    """
    # Инициализация объектов страниц
    login_page = LoginPage(browser)
    main_page = MainPage(browser)
    cart_page = CartPage(browser)
    checkout_page = CheckoutPage(browser)

    with allure.step("1. Открываем сайт и авторизуемся"):
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

    with allure.step("2. Добавляем товары в корзину"):
        items_to_add = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie"
        ]

        for item in items_to_add:
            main_page.add_to_cart(item)

    with allure.step("3. Переходим в корзину и начинаем оформление"):
        main_page.go_to_cart()
        cart_page.checkout()

    with allure.step("4. Заполняем данные и получаем итоговую сумму"):
        checkout_page.fill_info("Иван", "Петров", "123456")
        total = checkout_page.get_total()

    with allure.step("5. Проверяем итоговую сумму"):
        assert total == "Total: $58.29", f"Ожидалась сумма $58.29, получено {total}"