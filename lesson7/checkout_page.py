import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, browser):
        """
        Конструктор класса CheckoutPage, принимает объект браузера и сохраняет его в экземпляре класса.

        :param browser: Объект браузера (Selenium WebDriver), используемый для взаимодействия с веб-элементами.
        """
        self.browser = browser

    @allure.step("Заполнение информации о покупателе: {first_name} {last_name}, почтовый код: {postal_code}")
    def fill_info(self, first_name, last_name, postal_code):
        """
        Метод заполняет форму доставки заказа, передавая личные данные покупателя.

        :param first_name: Имя покупателя (строка).
        :param last_name: Фамилия покупателя (строка).
        :param postal_code: Почтовый индекс покупателя (строка).
        """
        with allure.step("Ввод имени"):
            self.browser.find_element(By.ID, "first-name").send_keys(first_name)
        with allure.step("Ввод фамилии"):
            self.browser.find_element(By.ID, "last-name").send_keys(last_name)
        with allure.step("Ввод почтового кода"):
            self.browser.find_element(By.ID, "postal-code").send_keys(postal_code)
        with allure.step("Нажатие кнопки 'Continue'"):
            self.browser.find_element(By.ID, "continue").click()

    @allure.step("Получение итоговой суммы заказа")
    def get_total(self):
        """
        Метод получает итоговую стоимость заказа, ожидаемую на странице подтверждения заказа.

        :return: Итоговая сумма заказа (строка).
        """
        with allure.step("Ожидание загрузки итоговой суммы"):
            WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
            )
        total = self.browser.find_element(By.CLASS_NAME, "summary_total_label").text
        allure.dynamic.description(f"Итоговая сумма: {total}")
        return total