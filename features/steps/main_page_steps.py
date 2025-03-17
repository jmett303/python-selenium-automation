from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep, process_time_ns

#Locators
SEARCH_FIELD = (By.ID, 'search')
SEARCH_BUTTON = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
HEADER_LINKS = (By.CSS_SELECTOR, '[data-test*="UtilityHeader"]')
SIGN_IN = (By.CSS_SELECTOR, '[data-test="@web/AccountLink"]')
SIGN_IN_2 = (By.CSS_SELECTOR, '[data-test="accountNav-signIn"]')


@given('Open target main page')
def open_target_main(context):
    context.driver.get('https://target.com/')


@when('Search for {product}')
def search_product(context, product):
    context.driver.find_element(*SEARCH_FIELD).send_keys(product)   # * = use all elements in parentheses
    context.driver.find_element(*SEARCH_BUTTON).click()
    sleep(10)


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


@then('Verify {link_amount} header links are shown')
def verify_6_header_links_shown(context, link_amount):
    link_amount = int(link_amount)
    links = context.driver.find_elements(*HEADER_LINKS)
    assert len(links) == 6, f'Expected {link_amount} header links, but got {len(links)}'
    print(links)
