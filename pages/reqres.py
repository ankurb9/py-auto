from playwright.sync_api import Page, Route, Request
import json
from utils.ui_actions import Action


class ReqRes:

    def __init__(self, page: Page):
        self.action = Action(page)
        self.action.navigate("https://reqres.in/")

    def get_resp(self):
        return json.loads(self.action.get_text("xpath=//pre[@data-key='output-response']"))

    def click_single_user(self):
        self.action.click("//a[text()=' Single user ']")

    def mock_single_user(self, user_data: dict):
        """Attach route to mock single user response."""
        self.action.change_response(url_pattern="**/api/users/2", user_data=user_data)

