from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

options = webdriver.ChromeOptions() 

download_path = os.getcwd()+ f"\\Downloads"

profile = {"plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}], # Disable Chrome's PDF Viewer
               "download.default_directory": os.getcwd()+f"\\Downloads" , "download.extensions_to_open": "applications/pdf", "plugins.always_open_pdf_externally": True}
options.add_experimental_option("prefs", profile)
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)
driver.get("https://intellipaat.com/blog/tutorial/selenium-tutorial/selenium-cheat-sheet/")
time.sleep(2)
print(driver.title)
driver.maximize_window()

download_loc = (By.XPATH, "//a[@href='https://intellipaat.com/blog/wp-content/uploads/2022/10/Selenium-Cheat-Sheet-2022.pdf']//child::strong[text()='Download a Printable PDF of this Cheat Sheet']")

driver.find_element(*download_loc).click()
wait = WebDriverWait(driver, 20)
wait.until(EC.number_of_windows_to_be(2))
driver.switch_to.window(driver.window_handles[1])
driver.close()
driver.switch_to.window(driver.window_handles[0])

while True:
    files = os.listdir(download_path)
    if any(file.endswith(".pdf") and file.startswith("Selenium")  for file in files):
        time.sleep(5)
        break

files = os.listdir(download_path)
for file in files:
    if file.startswith("Selenium"):
        os.remove(os.path.join(download_path, file))
        
driver.quit()





