from playwright.sync_api import Page
import json
from utils.ui_actions import Action


class ReqRes:

    def __init__(self, page: Page):
        self.action = Action(page)

    def response(self):
        return json.loads(self.action.get_text("xpath=//pre[@data-key='output-response']"))
