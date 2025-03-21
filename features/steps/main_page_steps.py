from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
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
    context.app.main_page.open_main_page()
    context.driver.wait.until(
        EC.element_to_be_clickable(SEARCH_FIELD),
        message='Search field not clickable'
    )


@when('Search for {search_word}')
def search_product(context, search_word):
    context.app.header.search(search_word)


@when('Click on cart icon')
def click_cart(context):
    # context.driver.find_element(*CART_ICON).click()
    context.app.main_page.click(*CART_ICON)


@when('Click sign in')
def click_sign_in(context):
    context.driver.find_element(*SIGN_IN).click()


@when('Click 2nd sign in')
def click_2nd_sign_in(context):
    context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_2)).click()


@then('Verify {link_amount} header links are shown')
def verify_6_header_links_shown(context, link_amount):
    link_amount = int(link_amount)
    links = context.driver.find_elements(*HEADER_LINKS)
    assert len(links) == 6, f'Expected {link_amount} header links, but got {len(links)}'
    print(links)