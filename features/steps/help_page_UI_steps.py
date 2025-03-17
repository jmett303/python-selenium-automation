from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep, process_time_ns

#Locators
TARGET_HELP = (By.CSS_SELECTOR,'.bio .custom-h2')
SEARCH_BOX = (By.CSS_SELECTOR, '.form-search')
HELP_OPTIONS = (By.CSS_SELECTOR, '.box-column')


@given('Open target help page')
def open_target_main(context):
    context.driver.get('https://help.target.com/help')

@then('Verify Help Header present on page')
def verify_help_header(context):
    context.driver.find_element(*TARGET_HELP)

@then('Verify search box present on page')
def verify_search_box(context):
    context.driver.find_element(*SEARCH_BOX)

@then('Verify Help options present on page')
def verify_help_options(context):
    context.driver.find_element(*HELP_OPTIONS)