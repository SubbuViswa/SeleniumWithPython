from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browserName ="edge"

if browserName == "chrome":
    driver = webdriver.Chrome()
elif browserName == "firefox":
    driver = webdriver.Firefox()
elif browserName == "edge":
    driver = webdriver.Edge()
else:
    print("Please enter the browser name:" + browserName)
    raise Exception('Driver is not found')

driver.implicitly_wait(5)
driver.get("https://www.google.com")
print(driver.title)
driver.maximize_window()
driver.find_element(By.NAME, 'q').send_keys("selenium")

time.sleep(2)
driver.quit()