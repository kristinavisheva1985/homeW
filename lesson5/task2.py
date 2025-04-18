from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Открытие страницы
driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/dynamicid")

button = driver.find_element(
    By.XPATH, "//button[contains(@class, 'btn-primary')]",
)
button.click()

time.sleep(2)

driver.quit()