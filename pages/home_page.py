from utils.ui_actions import Action
from pages.login_page import LoginPage


class HomePage(LoginPage):
    def __init__(self, page):

        super().__init__(page)
        super().successful_login()
        self.action = Action(page)

    def click(self, item_name):
        self.action.click(locator=f"xpath=//div[text()='{item_name}']/ancestor::div[@class='inventory_item_description']//button")

    def get_cart_badge_count(self):
        return int(self.action.get_text(locator="xpath=//a/span[@data-test='shopping-cart-badge']"))

    def is_badge_count_visible(self):
        return self.action.is_visible(locator="xpath=//a/span[@data-test='shopping-cart-badge']")


    def get_button_text(self, item_name):
        return self.action.get_text(
            locator=f"xpath=//div[text()='{item_name}']/ancestor::div[@class='inventory_item_description']//button")
