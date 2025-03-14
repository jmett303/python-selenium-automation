from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then("verify 'Your cart is empty' message is shown")
def verify_cart_empty(context):
    expected_result = 'Your cart is empty'
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
    assert expected_result == actual_result, f'Error. Text {expected_result} not in {actual_result}'