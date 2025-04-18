import pytest
from selenium import webdriver
from login_page import LoginPage
from main_page import MainPage
from cart_page import CartPage
from checkout_page import CheckoutPage


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_shopping_flow(browser):
    # Инициализация страниц
    login_page = LoginPage(browser)
    main_page = MainPage(browser)
    cart_page = CartPage(browser)
    checkout_page = CheckoutPage(browser)

    # 1. Открываем сайт и авторизуемся
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # 2. Добавляем товары в корзину
    items_to_add = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]

    for item in items_to_add:
        main_page.add_to_cart(item)

    # 3. Переходим в корзину и начинаем оформление
    main_page.go_to_cart()
    cart_page.checkout()

    # 4. Заполняем данные и получаем итоговую сумму
    checkout_page.fill_info("Иван", "Петров", "123456")
    total = checkout_page.get_total()

    # 5. Проверяем итоговую сумму
    assert total == "Total: $58.29", f"Ожидалась сумма $58.29, получено {total}"