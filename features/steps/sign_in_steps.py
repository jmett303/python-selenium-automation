from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


LOGIN_BUTTON = (By.CSS_SELECTOR, '#login')


@then('Verify Sign In form opened')
def verify_sign_in(context):
    context.driver.find_element(*LOGIN_BUTTON)
