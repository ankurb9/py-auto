from playwright.sync_api import Page
from utils.log import get_logger
from utils.context import Context

log = get_logger()
conf = Context()

class Action:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        self.page.goto(conf.url)

    def click(self, locator: str):
        self.page.click(locator)

    def fill(self, locator: str, value: str):
        self.page.fill(locator, value)

    def get_text(self, locator):
        return self.page.text_content(locator)

    def is_visible(self, locator: str):
        try:
            self.page.wait_for_selector(selector=locator, state="visible", timeout=10_000)
            return True
        except Exception as e:
            log.error(e)
            return False

