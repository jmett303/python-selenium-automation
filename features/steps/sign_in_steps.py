from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

@given('Open sign in page')
def open_sign_in_page(context):
    context.app.sign_in_page.open_sign_in_page()

@when('Click on Target terms and conditions link')
def click_tc_link(context):
    context.app.sign_in_page.click_tc_link()

@then('Verify Sign In form opened')
def verify_sign_in(context):
    context.app.sign_in_page.verify_sign_in_open()



