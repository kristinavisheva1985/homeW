from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

waiter = WebDriverWait(driver, 30)

pictures = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div#image-container.col-12.py-2 img#landscape"))
)

img = driver.find_element(By.CSS_SELECTOR, "#award")
print(img.get_attribute('src'))