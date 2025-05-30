import allure
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, browser):
        """
        Конструктор класса LoginPage, принимает объект браузера и сохраняет его в экземпляре класса.

        :param browser: Объект браузера (Selenium WebDriver), используемый для взаимодействия с веб-элементами.
        """
        self.browser = browser

    @allure.step("Открыть страницу авторизации")
    def open(self):
        """
        Открывает страницу авторизации по заданному URL.
        """
        self.browser.get("https://www.saucedemo.com/")

    @allure.step("Авторизация пользователя: логин '{username}'")
    def login(self, username, password):
        """
        Выполняет процедуру авторизации на сайте, заполняя поля логина и пароля и отправляя форму.

        :param username: Логин пользователя (строка).
        :param password: Пароль пользователя (строка).
        """
        with allure.step("Ввести логин"):
            self.browser.find_element(By.ID, "user-name").send_keys(username)

        with allure.step("Ввести пароль"):
            self.browser.find_element(By.ID, "password").send_keys(password)

        with allure.step("Нажать кнопку входа"):
            self.browser.find_element(By.ID, "login-button").click()