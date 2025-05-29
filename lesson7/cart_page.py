import allure
from selenium.webdriver.common.by import By


class CartPage:
    """
    Класс представляет страницу корзины товаров и описывает взаимодействие с элементами страницы.
    """

    def __init__(self, browser):
        """
        Конструктор класса CartPage.

        :param browser: Объект браузера Selenium WebDriver, используемый для взаимодействия с веб-элементами.
        """
        self.browser = browser

    @allure.step("Для перехода к оформлению заказа, нажать кнопку: {Checkout}")
    def checkout(self):
        """
        Метод предназначен для нажатия кнопки оформления заказа ("Checkout").

        Этот метод находит элемент с идентификатором 'checkout' и инициирует клик по нему,
        переходя таким образом к следующему этапу процесса покупки — странице оформления заказа.
        """
        self.browser.find_element(By.ID, "checkout").click()