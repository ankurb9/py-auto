from utils.ui_actions import Action
from utils.context import Context
from utils.log import get_logger

conf = Context()
log = get_logger()

class LoginPage:
    def __init__(self, page):
        log.info("Initiating action class.")
        self.action = Action(page)

    def navigate(self):
        self.action.navigate()

    def enter_username(self, user_name: str):
        self.action.fill(locator="xpath=//input[@id='user-name']", value=user_name)

    def enter_password(self, password: str):
        self.action.fill(locator="xpath=//input[@id='password']", value=password)

    def click_login_button(self):
        self.action.click(locator="xpath=//input[@id='login-button']")

    def verify_locked_text(self, text):
        assert self.action.get_text(locator="xpath=//h3[@data-test='error']") == text

    def verify_login(self):
        assert self.action.is_visible(locator="xpath=//a[@data-test='shopping-cart-link']"), "Login Failed"

    def simply_click_login(self, username=conf.username, password = conf.password):
        self.navigate()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def successful_login(self):
        self.simply_click_login()
        self.verify_login()
        log.info("Logged in successfully")








