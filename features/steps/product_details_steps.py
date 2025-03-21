from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

#Locators
COLOR_OPTIONS = (By.CSS_SELECTOR, 'div[aria-label="Carousel"] li img')
SELECTED_COLOR = (By.CSS_SELECTOR, '[data-test="@web/VariationComponent"]:nth-of-type(1)')

@given('Open Target product {product_id} page')
def open_target(context, product_id):
    context.driver.get(f'https://www.target.com/p/{product_id}')
    sleep(8)


@then('Verify user can click through colors')
def verify_colors(context):
    expected_colors = ['Blue', 'Cream', 'Light Pink']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)

    for color in colors:
        context.driver.wait.until(EC.element_to_be_clickable(color), message='Color not clickable')
        color.click()

        selected_color = context.driver.find_element(*SELECTED_COLOR).text
        selected_color = selected_color.split('\n')[1] #remove 'Color\n part, keep Black'

        actual_colors.append(selected_color)

    print('Expected colors:', expected_colors)
    print('Actual colors:', actual_colors)


    assert expected_colors == actual_colors, f'Expected {expected_colors} colors, got {actual_colors}'