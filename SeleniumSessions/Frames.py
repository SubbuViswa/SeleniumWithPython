from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://www.dummypoint.com/Frame.html")
driver.maximize_window()
iframeCount = driver.find_elements(By.TAG_NAME, "iframe")
print(len(iframeCount))
def promptAlertHandling():
    try:
        alertButton = driver.find_element(By.XPATH, '//button[text()="Promt Alert"]')
        alertButton.click()
        name = "Subbulakshmi"
        wait = WebDriverWait(driver,20)
        wait.until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.send_keys(name)
        alert.accept()
        time.sleep(2)
        promptText = driver.find_element(By.XPATH, "//p[@id='demo']")
        print(promptText.text.casefold())
        if promptText.text.lower() == "Hello ".lower() + name.lower() + "! " + "This is the text from promt alert".lower():
            print("Test passed")
        else:
            print("Test Failed")
    except Exception as e:
        print(e)

driver.switch_to.frame(0)
frameName = driver.find_element(By.ID,'framename')
print(frameName.text)
promptAlertHandling()

time.sleep(2)
driver.switch_to.default_content()
promptAlertHandling()

time.sleep(2)
driver.quit()
