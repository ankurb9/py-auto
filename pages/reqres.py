from playwright.sync_api import Page
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
