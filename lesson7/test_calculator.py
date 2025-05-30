import allure
import pytest
from selenium import webdriver
from calculator_page import CalculatorPage


@pytest.fixture
@allure.epic("Калькулятор")
@allure.title("Тестирование калькулятора")
@allure.severity("critical")
def browser():
    """
    Фикстура Pytest, создающая экземпляр браузера и предоставляющая его тестовым сценариям.

    Перед началом теста запускается новый экземпляр браузера Chrome, а после завершения теста закрывается окно браузера.

    :yield: Объект браузера (Selenium WebDriver).
    """
    with allure.step("Инициализация браузера"):
        driver = webdriver.Chrome()
        yield driver
    with allure.step("Закрытие браузера"):
        driver.quit()


@allure.feature("Проверка процессов и возможностей калькулятора")
@allure.story("Тест калькулятора с задержкой 45 сек")
def test_calculator_with_delay(browser):
    """
    Тестовый сценарий проверки работы онлайн-калькулятора с установленной временной задержкой.

    Последовательность действий:
    1. Открывается страница калькулятора.
    2. Устанавливается временная задержка перед выполнением вычислений (45 секунд).
    3. Производится последовательность арифметических операций (7+8).
    4. Проверяется правильность результата спустя установленное время ожидания (50 секунд).

    :param browser: Экземпляр браузера, предоставляемый фикстурой.
    """
    calculator = CalculatorPage(browser)

    with allure.step("1. Открываем страницу калькулятора"):
        calculator.open()

    with allure.step("2. Устанавливаем задержку 45 секунд"):
        calculator.set_delay(45)

    with allure.step("3. Нажимаем кнопки 7 + 8 ="):
        calculator.click_button('7')
        calculator.click_button('+')
        calculator.click_button('8')
        calculator.click_button('=')

    with allure.step("4. Получаем и проверяем результат, спустя 50 секунд"):
        result = calculator.get_result(50)  # Даем больше времени (50 секунд)
        assert result == "15", f"Ожидался результат 15, получено {result}"