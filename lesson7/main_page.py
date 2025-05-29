import allure
from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, browser):
        """
        Конструктор класса MainPage, принимает объект браузера и сохраняет его в экземпляре класса.

        :param browser: Объект браузера (Selenium WebDriver), используемый для взаимодействия с веб-элементами.
        """
        self.browser = browser

    @allure.step("Добавить товар '{item_name}' в корзину")
    def add_to_cart(self, item_name):
        """
        Добавляет указанный товар в корзину, находя соответствующую кнопку и выполняя клик.

        :param item_name: Название товара (строка), который нужно добавить в корзину.
        """
        item_xpath = f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button"
        with allure.step(f"Найти и нажать кнопку добавления для товара: {item_name}"):
            self.browser.find_element(By.XPATH, item_xpath).click()
        allure.dynamic.description(f"Товар '{item_name}' успешно добавлен в корзину")

    @allure.step("Перейти в корзину")
    def go_to_cart(self):
        """
        Перейти на страницу корзины покупок, нажав на соответствующий элемент интерфейса.
        """
        with allure.step("Нажать на иконку корзины"):
            self.browser.find_element(By.CLASS_NAME, "shopping_cart_link").click()