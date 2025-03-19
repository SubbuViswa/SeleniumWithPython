from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://testpages.eviltester.com/styled/challenges/growing-clickable.html")
time.sleep(2)
print(driver.title)
driver.maximize_window()

grow_btn_loc = (By.XPATH, "//button[@id='growbutton']")
grow_btn_status_loc = (By.XPATH, "//p[@id='growbuttonstatus']")

grown_btn_status = "Event Triggered"

wait = WebDriverWait(driver, 20)
wait.until(EC.text_to_be_present_in_element_attribute(grow_btn_loc, "class", "grown"))

driver.find_element(*grow_btn_loc).click()

click_status = driver.find_element(*grow_btn_status_loc).get_property("textContent")
assert click_status == grown_btn_status, f"Actual {click_status} is not equal to {grown_btn_status}"



