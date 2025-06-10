import pytest
from tests.Pages.loginPage import LoginPage
from Utilities import BaseClass
from tests.framework.app import APP

@pytest.fixture
def app():
    app = APP()
    yield app

@pytest.fixture
def loginPage(app):
    loginPage = LoginPage(app)
    yield loginPage