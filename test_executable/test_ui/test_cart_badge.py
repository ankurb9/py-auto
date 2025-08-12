from playwright.sync_api import Page
from pages.home_page import HomePage
from utils import log

def test_add_item_to_cart(page: Page):
    # login = LoginPage(page)
    home = HomePage(page)

    # login.successful_login()
    home.click("Sauce Labs Backpack")
    assert home.get_button_text("Sauce Labs Backpack") == "Remove", "Button text is not changed."
    assert home.get_cart_badge_count() == 1, "Shopping cart badge count doesn't match"

def test_add_and_remove_items(page: Page):
    # login = LoginPage(page)
    home = HomePage(page)

    # login.successful_login()
    home.click("Sauce Labs Backpack")
    home.click("Sauce Labs Backpack")
    assert home.get_button_text("Sauce Labs Backpack") == "Add to cart1", "Button text is not changed."

    assert not home.is_badge_count_visible(), "Items not removed from the cart"

def test_add_multiple_items_to_cart(page: Page):
    # login = LoginPage(page)
    home = HomePage(page)

    # login.successful_login()
    log.info("Adding 2 items to cart")
    home.click("Sauce Labs Backpack")
    home.click("Sauce Labs Bike Light")

    assert home.get_cart_badge_count() == 2, "Shopping cart badge count doesn't match"

