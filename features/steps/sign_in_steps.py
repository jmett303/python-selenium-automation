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

@when('Enter correct email: {email}')
def enter_correct_email(context, email):
    context.app.sign_in_page.enter_correct_email(email)

@when('Click continue')
def click_continue(context):
    context.app.sign_in_page.click_continue()

@when('Enter incorrect password: {password}') #Correct: Password123
def enter_incorrect_password(context, password):
    context.app.sign_in_page.enter_incorrect_password(password)

@when('Click Sign in button')
def click_sign_in_button(context):
    context.app.sign_in_page.click_sign_in_button()

@then('Verify Sign In form opened')
def verify_sign_in(context):
    context.app.sign_in_page.verify_sign_in_open()

@then('Verify error message is shown')
def verify_error_message(context):
    context.app.sign_in_page.verify_error_message()





