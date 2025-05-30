import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """Класс для работы со страницей калькулятора с задержкой выполнения операций."""

    def __init__(self, browser):
        """Инициализирует экземпляр страницы калькулятора.

        Args:
            browser: WebDriver - экземпляр веб-драйвера для взаимодействия с браузером
        """
        self.browser = browser
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.screen = (By.CSS_SELECTOR, ".screen")
        self.buttons = {
            '1': (By.XPATH, "//span[text()='1']"),
            '2': (By.XPATH, "//span[text()='2']"),
            '3': (By.XPATH, "//span[text()='3']"),
            '4': (By.XPATH, "//span[text()='4']"),
            '5': (By.XPATH, "//span[text()='5']"),
            '6': (By.XPATH, "//span[text()='6']"),
            '7': (By.XPATH, "//span[text()='7']"),
            '8': (By.XPATH, "//span[text()='8']"),
            '9': (By.XPATH, "//span[text()='9']"),
            '0': (By.XPATH, "//span[text()='0']"),
            '+': (By.XPATH, "//span[text()='+']"),
            '-': (By.XPATH, "//span[text()='-']"),
            '*': (By.XPATH, "//span[text()='×']"),
            '/': (By.XPATH, "//span[text()='÷']"),
            '=': (By.XPATH, "//span[text()='=']"),
            'C': (By.XPATH, "//span[text()='C']")
        }

    @allure.step("Открыть страницу калькулятора")
    def open(self):
        """Открывает страницу калькулятора в браузере.

        Возвращает:
            None
        """
        self.browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    @allure.step("Установить задержку {seconds}")
    def set_delay(self, seconds):
        """Устанавливает время задержки вычислений в секундах.

        Args:
            seconds: int|str - количество секунд задержки

        Возвращает:
            None
        """
        delay_field = self.browser.find_element(*self.delay_input)
        delay_field.clear()
        delay_field.send_keys(str(seconds))

    @allure.step("Нажать кнопку {button}")
    def click_button(self, button):
        """Нажимает указанную кнопку на калькуляторе.

        Args:
            button: str - символ кнопки (цифра 0-9 или оператор +, -, *, /, =, C)

        Возвращает:
            None
        """
        self.browser.find_element(*self.buttons[button]).click()

    @allure.step("Получить результат (таймаут {timeout} секунд)")
    def get_result(self, timeout):
        """Ожидает и возвращает результат вычислений.

        Args:
            timeout: int - максимальное время ожидания в секундах

        Возвращает:
            str - текстовое значение результата на экране калькулятора
        """
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.text_to_be_present_in_element(self.screen, "15")
            )
            result = self.browser.find_element(*self.screen).text
            allure.dynamic.description(f"Получен результат: {result}")
            return result
        except Exception as e:
            result = self.browser.find_element(*self.screen).text
            allure.dynamic.description(f"Ошибка при получении результата: {e}\nТекущее значение: {result}")
            return result