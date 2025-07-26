
from playwright.sync_api import Page
from utils.context import Context
from utils.log import get_logger
from pages.login_page import LoginPage

ctx = Context()
log = get_logger()

def test_login_happy_path(page: Page):
    login = LoginPage(page=page)

    login.successful_login()
    login.verify_login()

def test_locked_user_message(page: Page):
    login = LoginPage(page=page)
    login.navigate()
    login.enter_username("locked_out_user")
    login.enter_password("secret_sauce")
    login.click_login_button()
    login.verify_locked_text("Epic sadface: Sorry, this user has been locked out.")