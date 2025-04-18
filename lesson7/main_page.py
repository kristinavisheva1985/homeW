from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, browser):
        self.browser = browser

    def add_to_cart(self, item_name):
        item_xpath = f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button"
        self.browser.find_element(By.XPATH, item_xpath).click()

    def go_to_cart(self):
        self.browser.find_element(By.CLASS_NAME, "shopping_cart_link").click()
 30 changes: 30 additions & 0 deletions30
07_lesson/test_calculator.py
