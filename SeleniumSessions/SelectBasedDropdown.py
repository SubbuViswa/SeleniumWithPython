from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://www.orangehrm.com/en/30-day-free-trial")
print(driver.title)
driver.maximize_window()
time.sleep(2)


def select_option_with_select(option,element, value):
    if option == "Select By Visible Text":
        element.click()
        select = Select(element)
        select.select_by_visible_text(value)
    elif option == "Select By Index":
        element.click()
        select = Select(element)
        select.select_by_index(value)
    elif option == "Select By Value":
        element.click()
        select = Select(element)
        select.select_by_value(value)
    else:
        print("Please select a valid option")

def select_from_list(option,elements, value):
    option.click()
    for element in elements:
        if element.text == value:
            element.click()
            break


countryOption = driver.find_element(By.XPATH, "//select[@name='Country']")
countryList = driver.find_elements(By.XPATH, "//select[@name='Country']/option")
select_option_with_select("Select By Visible Text",countryOption, "Albania")
select_option_with_select("Select By Index",countryOption, 15)
select_option_with_select("Select By Value",countryOption, "Cameroon")
select_from_list(countryOption,countryList, "Hong Kong")
