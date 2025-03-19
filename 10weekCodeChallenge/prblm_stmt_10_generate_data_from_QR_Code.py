from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pyzbar.pyzbar import decode
from PIL import Image
import cv2
import imageio.v2 as imageio
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://qaplayground.dev/apps/qr-code-generator/")
time.sleep(2)
print(driver.title)
driver.maximize_window()

text_input_loc = (By.XPATH, "//input[@type='text']")
generate_qr_btn_loc = (By.XPATH, "//button[text()='Generate QR Code']")
qr_code_loc = (By.XPATH, "//div[@class='qr-code']//img")

input_text = "I am Test automation Engineer"

driver.find_element(*text_input_loc).clear()

driver.find_element(*text_input_loc).send_keys(input_text)
driver.find_element(*generate_qr_btn_loc).click()

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located(qr_code_loc))

url = driver.find_element(*qr_code_loc).get_property("src")
print(url)

qrcode = imageio.imread(url)
data = decode(qrcode)
qr_code_val = data[0].data.decode("utf-8")
print(qr_code_val)

assert input_text == qr_code_val, f"The displayed {qr_code_val} is not matching {input_text}"



#print(qrcode)
#img = cv2.imread(qrcode, 2)
#print(img)
#qrdata = decode(qrcode)
#print(qrdata)