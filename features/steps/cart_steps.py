
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


CART_ITEMS = (By.CSS_SELECTOR, '[data-test="cartItem"]')


@then("verify 'Your cart is empty' message is shown")
def verify_cart_empty(context):
    expected_result = 'Your cart is empty'
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
    assert expected_result == actual_result, f'Error. Text {expected_result} not in {actual_result}'


@then('Verify item added to cart')
def verify_item_added(context):
    cart_items = context.driver.find_elements(*CART_ITEMS)
    assert len(cart_items) == 1, f'Error. Expected 1 item in cart but got {len(cart_items)}'
    print(f'{len(cart_items)} item(s) in cart')
