from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, allure
from Config import config
#from Utilities import BaseClass


class LoginPage():

    #Locators
    submit_button = (By.XPATH, "//button[@id='submit']")
    success_login_msg = (By.XPATH, "//div[@class='post-header']//h1")
    error_loc = "//div[@id='error']"
    user_name_loc = "//input[@name='username']"
    password_loc = "//input[@name='password']"

    def __init__(self, app):
        self.driver = app.driver

    def getLoginPage(self):
        self.navigate_to_url(config.URL) 
   
    def enterUserCredentials(self, username, password):
        self.input_text(self.user_name_loc,username)
        self.input_text(self.password_loc,password)
        self.find_and_click_an_element(self.submit_button)

    def validateSuccessLoginMessage(self, text):
        successful_login_txt = self.get_text(self.success_login_msg)
        assert successful_login_txt == text

    def validateLoginError(self, error):
        time.sleep(self.s_delay)
        error_text = self.get_property_value(self.error_loc)
        assert error_text == error