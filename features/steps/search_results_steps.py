from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


from selenium.webdriver.common.devtools.v131.css import CSSLayer

ADD_TO_CART = (By.CSS_SELECTOR, '[index="0"] [id*="addToCart"]')
PRODUCT_NAME = (By.CSS_SELECTOR, '[data-test="content-wrapper"] h4')
PRODUCT_NAME_IN_CART = (By.CSS_SELECTOR, '[data-test="cartItem-title"]')
ADD_TO_CART_2 = (By.CSS_SELECTOR, '[data-test="orderPickupButton"]')
VIEW_CART = (By.CSS_SELECTOR, '[href="/cart"]')
SEARCH_RESULTS_TEXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")
CART_ITEMS = (By.CSS_SELECTOR, '[data-test="cartItem"]')


@when('Add to cart')
def add_item_to_cart(context):
    # context.driver.find_element(*ADD_TO_CART).click()
    context.driver.wait.until(EC.element_to_be_clickable(ADD_TO_CART), message='Add to cart button not clickable')
    context.driver.find_elements(*ADD_TO_CART)[0].click() #selects first item



@when('Store product name')
def store_product_name(context):
    context.driver.wait.until(
        EC.visibility_of_element_located(PRODUCT_NAME),
        #####do not use * with locator for EC library!
        message='Product name not visible'
    )
    context.product_name = context.driver.find_element(*PRODUCT_NAME).text
    print('Product name stored: ', context.product_name)


@when('Confirm add to cart')
def add_item_to_cart(context):
    context.driver.wait.until(EC.element_to_be_clickable(ADD_TO_CART_2),
    message='Second add to cart in navigation pop up window not clickable'
    )
    context.driver.find_element(*ADD_TO_CART_2).click()


@when('Navigate to Cart')
def search_results(context):
    context.driver.find_element(*VIEW_CART).click()
    sleep(5)


@then('Verify cart has correct product')
def verify_product_name(context):
    product_name_in_cart = context.driver.find_element(*PRODUCT_NAME_IN_CART).text
    assert product_name_in_cart[:20] == context.product_name[:20], \
        f'Error. Expected {context.product_name} but got {product_name_in_cart}'


@then('Verify correct search results shown for {expected_text}')
def verify_search_results(context, expected_text):
    actual_text = context.driver.find_element(*SEARCH_RESULTS_TEXT).text
    assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'

