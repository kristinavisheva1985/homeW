import pytest
from selenium import webdriver
from calculator_page import CalculatorPage


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_calculator_with_delay(browser):
    calculator = CalculatorPage(browser)

    # 1. Открываем страницу калькулятора
    calculator.open()

    # 2. Устанавливаем задержку 45 секунд
    calculator.set_delay(45)

    # 3. Нажимаем кнопки 7 + 8 =
    calculator.click_button('7')
    calculator.click_button('+')
    calculator.click_button('8')
    calculator.click_button('=')

    # 4. Получаем и проверяем результат
    result = calculator.get_result(50)  # Даем больше времени (50 секунд)
    assert result == "15", f"Ожидался результат 15, получено {result}"