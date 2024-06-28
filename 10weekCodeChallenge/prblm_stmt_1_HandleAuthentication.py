from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
time.sleep(2)
print(driver.title)
driver.maximize_window()

driver.quit()