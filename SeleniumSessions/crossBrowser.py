from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browserName = "safari"

if browserName == "chrome":
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
elif browserName == "firefox":
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
elif browserName == "edge":
    driver = webdriver.Edge()
else:
    print("Please enter a valid browser")
    raise Exception('Driver is not found')

driver.implicitly_wait(5)
driver.get("https://www.google.com")
print(driver.title)
driver.maximize_window()
driver.find_element(By.NAME, 'q').send_keys("selenium")

time.sleep(2)
driver.quit()