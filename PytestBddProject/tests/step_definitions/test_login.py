import pytest
 
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.by import By 
from tests.framework.fixture import loginPage
from tests.framework.fixture import app

# Scenarios
scenarios('../features/Login.feature')
 
 
# Fixtures
#@pytest.fixture
#def driver():
#    driver = webdriver.Chrome()
#    driver.implicitly_wait(TIMEOUT)
#    driver.maximize_window()
#    yield driver
#    driver.quit()
 
 
# Given Steps
@given('User is on login page')
def open_browser(loginPage):
    loginPage.getLoginPage()
 
# When Steps
@when(parsers.parse('User enter username "{username}" and password "{password}"'))
def enter_login_credentials(loginPage, username, password):
    loginPage.enterUserCredentials(username,password)
 
# Then Steps
@then(parsers.parse('User should be able to login successfully and new page open "{text}"'))
def validate_successful_login(loginPage, text):
    loginPage.validateSuccessLoginMessage(text)

# Then Steps
@then(parsers.parse('User should get the error "{error}"'))
def validateLoginError(loginPage, error):
    loginPage.validateLoginError(error)