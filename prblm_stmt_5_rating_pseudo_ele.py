from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://play1.automationcamp.ir/advanced.html")
time.sleep(2)
print(driver.title)
driver.maximize_window()

#static values for validation
placeholder_value = "Enter the * Rating of the book. E.g. ****"
success_text = "Well done!"

#locators
star_rating_loc = (By.XPATH, "//label[@class='star-rating']")
rating_loc = (By.XPATH, "//input[@id='txt_rating']")
check_rating_loc = (By.XPATH, "//button[@id='check_rating']")
validate_rating_loc = (By.XPATH, "//span[@id='validate_rating']")

#code
star_rating = str(driver.execute_script("return window.getComputedStyle(document.querySelector('label.star-rating'),':after').getPropertyValue('content')"))
enter_rating_placeholder = driver.find_element(*rating_loc).get_attribute("placeholder")
assert enter_rating_placeholder == placeholder_value , f"Expected {enter_rating_placeholder} does not match actual{placeholder_value}"
driver.find_element(*rating_loc).send_keys(star_rating.strip("\""))
driver.find_element(*check_rating_loc).click()
assert driver.find_element(*validate_rating_loc).is_displayed()
validation_text = driver.find_element(*validate_rating_loc).text
time.sleep(5)
assert validation_text == success_text , f"Expected {validation_text} does not match actual {success_text}"