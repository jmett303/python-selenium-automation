from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.devtools.v131.css import CSSLayer

ADD_TO_CART = (By.CSS_SELECTOR, '[index="0"] [id*="addToCart"]')
ADD_TO_CART_2 = (By.CSS_SELECTOR, '[data-test="orderPickupButton"]')
VIEW_CART = (By.CSS_SELECTOR, '[href="/cart"]')
SEARCH_RESULTS_TEXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")
CART_ITEMS = (By.CSS_SELECTOR, '[data-test="cartItem"]')


@when('Add {item} to cart')
def add_item_to_cart(context, item):
    context.driver.find_element(*ADD_TO_CART).click()
    context.driver.find_element(*ADD_TO_CART_2).click()


@when('Navigate to Cart')
def search_results(context):
    context.driver.find_element(*VIEW_CART).click()
    sleep(5)


@then('Verify correct search results shown for {expected_text}')
def verify_search_results(context, expected_text):
    actual_text = context.driver.find_element(*SEARCH_RESULTS_TEXT).text
    assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'


@then('Verify item added to cart')
def verify_item_added(context):
    cart_items = context.driver.find_elements(*CART_ITEMS)
    assert len(cart_items) >= 1, f'Error. Expected >= 1 item in cart but got {len(cart_items)}'
    print(f'{len(cart_items)} item(s) in cart')