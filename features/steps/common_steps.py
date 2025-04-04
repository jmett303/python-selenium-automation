from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

@given('Store original window')
def store_original_window(context):
    context.original_window = context.app.base_page.get_current_window_handle()
    print('Original_window:', context.original_window)

@when('Switch to new window')
def switch_to_new_window(context):
    context.app.base_page.switch_to_new_window()

@then('Close current page')
def close_page(context):
    context.app.base_page.close()

@then('Return to original window')
def switch_to_original_window(context):
    context.app.base_page.switch_to_window_by_id(context.original_window)