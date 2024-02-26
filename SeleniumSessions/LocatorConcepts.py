from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://classic.crmpro.com/")
#To find the title
print(driver.title)
#To find the total links
linkList = driver.find_elements(By.TAG_NAME,'a')
print(len(linkList))
#To find the total images and alt attribute
imageList = driver.find_elements(By.TAG_NAME,'img')
print(len(imageList))

for ele in imageList:
    print(ele.get_attribute('alt'))
#Different Locators
driver.find_element(By.NAME, "username").send_keys("username")
driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys("password")
driver.find_element(By.XPATH,"//input[@value='Login']").click()

time.sleep(10)
driver.quit()
