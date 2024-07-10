from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
first_name_loc = (By.XPATH, "//input[@id='fname']")
password_loc = (By.XPATH, "//input[@id='pass']")
pass_new_loc = (By.XPATH, "//input[@id='passnew']")
show_me_btn = (By.XPATH, "//input[@value='Show me']")
password = "Subbu123"
driver.implicitly_wait(5)
driver.get("https://seleniumpractise.blogspot.com/2016/09/how-to-work-with-disable-textbox-or.html")
time.sleep(2)
print(driver.title)
driver.maximize_window()
driver.find_element(*first_name_loc).send_keys("Subbu")
driver.execute_script("document.querySelector(\"input[id='pass']\").disabled = false");
driver.find_element(*password_loc).send_keys(password)



