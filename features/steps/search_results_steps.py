from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

from selenium.webdriver.common.devtools.v131.css import CSSLayer

SEARCH_RESULTS_TEXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")
CART_ITEMS = (By.CSS_SELECTOR, '[data-test="cartItem"]')


@when('Add to cart')
def add_item_to_cart(context):
    context.app.search_results.add_item_to_cart()


@when('Store product name')
def store_product_name(context):
    context.app.side_menu.store_product_name()


@when('Confirm add to cart')
def add_item_to_cart(context):
    context.app.side_menu.confirm_add_to_cart()


@when('Navigate to Cart')
def search_results(context):
    context.app.side_menu.navigate_to_cart()


@then('Verify cart has correct product')
def verify_product_name(context):
    context.app.side_menu.verify_product_name()


@then('Verify correct search results shown for {expected_text}')
def verify_search_results(context, expected_text):
    context.app.search_results.verify_search_results(expected_text)


@then('Verify {expected_text} in URL')
def verify_results_url(context, expected_text):
    context.app.search_results.verify_results_url(expected_text)
