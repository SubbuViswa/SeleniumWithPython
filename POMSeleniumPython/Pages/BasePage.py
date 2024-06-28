from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

"""This is the base class for all pages"""


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def do_click(self, byLocator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(byLocator)).click()

    def do_send_keys(self, byLocator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(byLocator)).send_keys(text)

    def get_text(self, byLocator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(byLocator))
        return element.text

    def get_attribute(self, byLocator, attribute):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(byLocator))
        return element.get_attribute(attribute)

    def is_visible(self, byLocator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(byLocator))
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title
