from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://www.google.com")
print(driver.title)
driver.maximize_window()
driver.find_element(By.NAME,'q').send_keys("selenium")
optionList = driver.find_elements(By.CSS_SELECTOR,'ul.G43f7e li')

for ele in optionList:
    if ele.text == "selenium tutorial":
        ele.click()
        break

time.sleep(5)
driver.quit()

