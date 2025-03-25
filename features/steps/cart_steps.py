from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify item added to cart')
def verify_item_added(context):
    context.app.cart_page.verify_item_added_to_cart()


@then("Verify 'Your cart is empty' message is shown")
def verify_cart_empty(context):
    context.app.cart_page.verify_cart_is_empty()


@then('Verify cart page opens')
def verify_cart_page_opens(context):
    context.app.cart_page.verify_cart_page_opens()