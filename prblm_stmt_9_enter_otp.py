from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://qaplayground.dev/apps/verify-account/")
time.sleep(2)
print(driver.title)
driver.maximize_window()

otp_input_elements = (By.XPATH, "//input[@type='number']")
otp_value = (By.XPATH, "//small[@class='info']")
otp_accepted_msg = (By.XPATH, "//small[text()='Success']")

success_msg = "Success"

otp_result = driver.find_element(*otp_value).get_property("textContent")

result = otp_result.replace("-","").split()
for str in result:
    if str.isdigit():
        str_result = str
ch_val = []
for ch in str_result:
    ch_val.append(ch)

print(ch_val)
i=0
input_elements = driver.find_elements(*otp_input_elements)

for input_element in input_elements:
    for i in range(1,len(ch_val)):
        if ch == '0':
            input_element.send_keys(Keys.NUMPAD0)
            break
        elif ch== '1':
            input_element.send_keys(Keys.NUMPAD1)
            break
        elif ch== '2':
            input_element.send_keys(Keys.NUMPAD2)
            break
        elif ch== '3':
            input_element.send_keys(Keys.NUMPAD3) 
            break
        elif ch== '4':
            input_element.send_keys(Keys.NUMPAD4) 
            break  
        elif ch== '5':
            input_element.send_keys(Keys.NUMPAD5)
            break
        elif ch== '6':
            input_element.send_keys(Keys.NUMPAD6)
            break
        elif ch== '7':
            input_element.send_keys(Keys.NUMPAD7)
            break
        elif ch== '8':
            input_element.send_keys(Keys.NUMPAD8) 
            break
        elif ch== '9':
            input_element.send_keys(Keys.NUMPAD9)
            break   
        i+=1
    
success_result = driver.find_element(*otp_accepted_msg).get_property("textContent")
assert success_result == success_msg, f"Success message {success_result} not displayed as expected {success_msg}"