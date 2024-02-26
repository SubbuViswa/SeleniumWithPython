from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
driver.implicitly_wait(5)
#driver.get("https://www.spicejet.com")
driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()
driver.implicitly_wait(5)

action = ActionChains(driver)
time.sleep(2)
#========================================================================================
#DragAndDrop
#source=driver.find_element(By.ID,"draggable")
#target=driver.find_element(By.ID,"droppable")
#action.click_and_hold(source)
#action.move_to_element(target)
#action.release(target).perform()
#action.drag_and_drop(source, target).perform()
#wait = WebDriverWait(driver,10)
#wait.until(EC.visibility_of_element_located((By.XPATH,"//p[text()='Dropped!']")))
#driver.quit()
#add_ons_selection = driver.find_element(By.XPATH,"//div[text()='Add-ons']")
#=======================================================================================
#Move To Element
#action = ActionChains(driver)
#action.move_to_element(add_ons_selection).perform()
#add_ons_spicelock = driver.find_element(By.XPATH,"//div[text()='SpiceLock']")
#add_ons_spicelock.click()
#======================================================================================
#Right-Click
contextMenu=driver.find_element(By.XPATH, "//span[text()='right click me']")
action.context_click(contextMenu).perform()
time.sleep(2)
context_list=driver.find_elements(By.XPATH, "//ul//li[contains(@class,'context-menu-item')]//span")
for menu in context_list:
    if menu.text == "Copy":
        menu.click()
        break

try:
    wait = WebDriverWait(driver,20)
    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()
    print("alert accepted")

except TimeoutException:
    print("No alert")

time.sleep(3)
driver.quit()
