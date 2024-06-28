from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    SUCCESS_MESSAGE = (By.XPATH, "//div[@class='post-content']//strong")
    LOGO = (By.XPATH, "//img[@alt='Practice Test Automation']")

    def __init__(self, driver):
        super().__init__(driver)

    def get_home_page_title(self, title):
        return self.get_title(title)

    def is_logo_available(self):
        return self.is_visible(self.LOGO)

    def get_logo_text(self):
        if self.is_visible(self.LOGO):
            return self.get_attribute(self.LOGO, "alt").strip()

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)

