import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_form_validation(browser):
    # Открываем страницу
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Заполняем форму
    browser.find_element(By.CSS_SELECTOR, 'input[name="first-name"]').send_keys("Иван")
    browser.find_element(By.CSS_SELECTOR, 'input[name="last-name"]').send_keys("Петров")
    browser.find_element(By.CSS_SELECTOR, 'input[name="address"]').send_keys("Ленина, 55-3")
    browser.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]').send_keys("test@skypro.com")
    browser.find_element(By.CSS_SELECTOR, 'input[name="phone"]').send_keys("+7985899998787")
    browser.find_element(By.CSS_SELECTOR, 'input[name="zip-code"]').send_keys("")  # Оставляем пустым
    browser.find_element(By.CSS_SELECTOR, 'input[name="city"]').send_keys("Москва")
    browser.find_element(By.CSS_SELECTOR, 'input[name="country"]').send_keys("Россия")
    browser.find_element(By.CSS_SELECTOR, 'input[name="job-position"]').send_keys("QA")
    browser.find_element(By.CSS_SELECTOR, 'input[name="company"]').send_keys("SkyPro")

    # Нажимаем кнопку Submit
    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    # Ждем, пока форма обновится (zip-code станет div с alert-danger)
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#zip-code.alert-danger")))

    # Проверяем, что zip-code подсвечен красным
    zip_code_alert = browser.find_element(By.CSS_SELECTOR, "#zip-code")
    assert "alert-danger" in zip_code_alert.get_attribute("class")

    # Проверяем, что остальные поля подсвечены зеленым
    fields_to_check = [
        'first-name', 'last-name', 'address', 'e-mail',
        'phone', 'city', 'country', 'job-position', 'company'
    ]

    for field_name in fields_to_check:
    # Теперь ищем div с id="field-name" (а не input)
        field = browser.find_element(By.CSS_SELECTOR, f"#{field_name}")
    assert "alert-success" in field.get_attribute("class"), f"Поле {field_name} не подсвечено зеленым"