from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

@then('Verify Terms and Conditions page is opened')
def verify_tc_page_open(context):
    context.app.t_and_c_page.verify_tc_page_open()