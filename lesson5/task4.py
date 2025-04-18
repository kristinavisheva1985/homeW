from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Шаг 1: Открытие страницы
driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")

try:
    # Шаг 2: Заполнение полей формы авторизации
    username_input = (WebDriverWait(driver, 10).until
                      (EC.presence_of_element_located
                       ((By.ID, "username"))))
    username_input.send_keys("tomsmith")

    password_input = (WebDriverWait(driver, 10).until
                      (EC.presence_of_element_located
                       ((By.ID, "password"))))
    password_input.send_keys("SuperSecretPassword!")

    # Шаг 3: Нажатие на кнопку Login
    login_button = (WebDriverWait(driver, 10).until
                    (EC.element_to_be_clickable
                     ((By.CSS_SELECTOR, ".radius"))))
    login_button.click()
finally:
    # Закрываем браузер после завершения работы
    driver.quit()