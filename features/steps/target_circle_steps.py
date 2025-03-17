from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep, process_time_ns


#locators
BENEFIT_CELLS = (By.CSS_SELECTOR, '.cell-item-content')


@given('Open target circle page')
def open_target_circle(context):
    context.driver.get('https://www.target.com/circle')


@then('Verify at least {cell_amt} benefit cells shown')
def verify_benefit_cells(context, cell_amt):
    cell_amt = int(cell_amt)
    benefit_cells = context.driver.find_elements(*BENEFIT_CELLS)
    assert len(benefit_cells) >= 10, f'Expected {cell_amt} benefit cells, but got {len(benefit_cells)}'
    print(f'Number of benefit cells found = {len(benefit_cells)}')