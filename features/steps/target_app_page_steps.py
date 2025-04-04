from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep


@given('Open Target App page')
def open_target_app(context):
    context.app.target_app_page.open_target_app()

@when('Click Privacy Policy link')
def click_pp_link(context):
    context.app.target_app_page.click_pp_link()

@then('Verify Privacy Policy page opened')
def verify_pp_opened(context):
    context.app.target_app_page.verify_pp_opened()
