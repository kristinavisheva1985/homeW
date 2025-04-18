from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/textinput")

text_input = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "newButtonName"))
)
text_input.clear()
text_input.send_keys("SkyPro")

button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#updatingButton"))
)
button.click()

updated_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#updatingButton"))
)
btn_text = updated_button.text
print(btn_text)

driver.quit()