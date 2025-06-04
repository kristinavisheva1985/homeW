import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 35)

    # Локаторы
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[data-testid='search-input']")
    SEARCH_BUTTON = (By.XPATH, "//span[text()='Найти']")
    OSTRICH_BANNER = (By.CSS_SELECTOR, "div.AppLogo_root.AppLogo_root-d4")
    ALL_SHOPS_BUTTON = (By.XPATH, "//button[@aria-label='Все Магазины']")
    DELIVERY_BUTTON = (By.XPATH, "//span[contains(@class, 'a1d1jd5y') and contains(., 'Укажите адрес доставки')]")
    WHERE_TO_DELIVER_BTN = (By.XPATH, "//div[contains(@class, 'UiKitSuperViewButton_textWrapper') and contains(., 'Куда доставить?')]")
    MODAL_WINDOW = (By.CSS_SELECTOR, "div.hs8s3dy")

    # Методы
    @allure.step("Ввести текст в поле поиска")
    def search_product(self, text):
        search_input = self.wait.until(EC.presence_of_element_located(self.SEARCH_INPUT))
        search_input.clear()
        search_input.send_keys(text)
        return search_input.get_attribute("value") == text

    @allure.step("Кликнуть на кнопку поиска")
    def click_search_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_BUTTON)).click()

    @allure.step("Кликнуть на баннер страуса")
    def click_ostrich_banner(self):
        self.wait.until(EC.element_to_be_clickable(self.OSTRICH_BANNER)).click()

    @allure.step("Кликнуть на баннер Магнита")
    def click_magnit_banner(self):
        self.wait.until(EC.element_to_be_clickable(self.MAGNIT_BANNER)).click()
        return True

    @allure.step("Кликнуть на кнопку 'Все магазины'")
    def click_all_shops_button(self):
        self.wait.until(EC.element_to_be_clickable(self.ALL_SHOPS_BUTTON)).click()
        return True  # Возвращаем True, если клик прошел успешно

    @allure.step("Кликнуть на кнопку 'Укажите адрес доставки'")
    def click_delivery_address(self):
        self.wait.until(EC.element_to_be_clickable(self.DELIVERY_BUTTON)).click()
        try:
            self.wait.until(EC.element_to_be_clickable(self.WHERE_TO_DELIVER_BTN)).click()
        except:
            pass
        (self.wait.until(EC.visibility_of_element_located(self.MODAL_WINDOW)))