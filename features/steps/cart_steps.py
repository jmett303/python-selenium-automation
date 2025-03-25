
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


CART_ITEMS = (By.CSS_SELECTOR, '[data-test="cartItem"]')


@then('Verify item added to cart')
def verify_item_added(context):
    cart_items = context.driver.find_elements(*CART_ITEMS)
    assert len(cart_items) == 1, f'Error. Expected 1 item in cart but got {len(cart_items)}'
    print(f'{len(cart_items)} item(s) in cart')


@then("Verify 'Your cart is empty' message is shown")
def verify_cart_empty(context):
    context.app.cart_page.verify_cart_is_empty()


@then('Verify cart page opens')
def verify_cart_page_opens(context):
    context.app.cart_page.verify_cart_page_opens()