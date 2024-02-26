from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://www.dummypoint.com/Frame.html")
iframeCount = driver.find_elements(By.TAG_NAME, "iframe")
print(len(iframeCount))
driver.switch_to.frame(0)
frameName = driver.find_element(By.ID,'framename')
print(frameName.text)


