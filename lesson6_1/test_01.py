from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://www.uitestingplayground.com/ajax")

button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#ajaxButton"))
)
button.click()

waiter = WebDriverWait(driver, 25)
waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".bg-success"), "Data loaded with AJAX get request.")
)

content = driver.find_element(By.CSS_SELECTOR, ".bg-success")
txt = content.text
print(txt)

driver.quit()