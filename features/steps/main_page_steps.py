from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

#Locators
SEARCH_FIELD = (By.ID, 'search')
SEARCH_BUTTON = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
SIGN_IN = (By.CSS_SELECTOR, '[data-test="@web/AccountLink"]')
SIGN_IN_2 = (By.CSS_SELECTOR, '[data-test="accountNav-signIn"]')


@given('Open target main page')
def open_target_main(context):
    context.driver.get('https://target.com/')


@when('Search for {product}')
def search_product(context, product):
    context.driver.find_element(*SEARCH_FIELD).send_keys(product)   # * = use all elements in parentheses
    context.driver.find_element(*SEARCH_BUTTON).click()
    sleep(6)


@when('Click on cart icon')
def click_cart(context):
    context.driver.find_element(*CART_ICON).click()


@when('Click sign in')
def click_sign_in(context):
    context.driver.find_element(*SIGN_IN).click()
    sleep(1)

@when('Click 2nd sign in')
def click_2nd_sign_in(context):
    context.driver.find_element(*SIGN_IN_2).click()
    sleep(1)