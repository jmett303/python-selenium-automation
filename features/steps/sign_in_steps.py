from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

#Locators
LOGIN_BUTTON = (By.CSS_SELECTOR, '#login')


@then('Verify Sign In form opened')
def verify_sign_in(context):
    context.driver.wait.until(EC.element_to_be_clickable(LOGIN_BUTTON))