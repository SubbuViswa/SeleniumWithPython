import allure
import pytest

from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest

class Test_Login(BaseTest):
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_page_title(self):
        self.loginPage = LoginPage(self.driver)
        loginTitle = self.loginPage.get_login_title(TestData.LOGIN_PAGE_TITLE)
        assert loginTitle == TestData.LOGIN_PAGE_TITLE

    @allure.severity(allure.severity_level.NORMAL)
    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USERNAME,TestData.PASSWORD)
