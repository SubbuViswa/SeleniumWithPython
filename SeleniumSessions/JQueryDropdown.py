from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def select_values(options,values):
    if not values[0] == 'all':
        for option in options:
            for value in range(len(values)):
                if option.text == values[value]:
                    option.click()
                    break
    else:
        try:
            for option in options:
                option.click()
        except Exception as e:
            print(e)

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")

driver.find_element(By.CSS_SELECTOR, "#justAnInputBox").click()
time.sleep(3)
drop_list = driver.find_elements(By.XPATH,"//span[contains(@class,'comboTreeItemTitle')]")
values_list = ['all']
#select_values(drop_list,["choice 2","choice 6","choice 6 2 1"])
select_values(drop_list,values_list)

driver.quit()