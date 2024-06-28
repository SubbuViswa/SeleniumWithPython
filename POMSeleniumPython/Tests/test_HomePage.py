import pytest

from Config.config import TestData
from Tests.test_base import BaseTest
from Pages.LoginPage import LoginPage
import allure


#@pytest.mark.usefixtures("log_on_failure")
@allure.severity(allure.severity_level.NORMAL)
class TestHomePage(BaseTest):
    def test_home_page_title(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USERNAME, TestData.PASSWORD)
        homePageTitle = homePage.get_home_page_title(TestData.HOME_PAGE_TITLE)
        assert homePageTitle == TestData.HOME_PAGE_TITLE

    def test_home_page_logo_text(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USERNAME, TestData.PASSWORD)
        logoText = homePage.get_logo_text()
        assert logoText == TestData.LOGO_TEXT

    def test_logo(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USERNAME, TestData.PASSWORD)
        assert homePage.is_logo_available()

    def test_username_in_success_message(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USERNAME, TestData.PASSWORD)
        successText = homePage.get_success_message()
        assert successText.find(TestData.USERNAME)
