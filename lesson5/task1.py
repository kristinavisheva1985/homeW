from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Открыть ссылку
driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/classattr")

# Поиск и клик по очень синей кнопке
blue_button = driver.find_element(By.CSS_SELECTOR, '.btn-primary')
blue_button.click()

# Ожидание завершения загрузки
time.sleep(2)

# Закрытие браузера
driver.quit()