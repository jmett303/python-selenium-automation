from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


SEARCH_RESULTS_TEXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")
CART_ITEMS = (By.CSS_SELECTOR, '[data-test="cartItem"]')
LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
PRODUCT_IMG = (By.CSS_SELECTOR, 'img')

@when('Add to cart')
def add_item_to_cart(context):
    context.app.search_results.add_item_to_cart()


@when('Store product name')
def store_product_name(context):
    context.app.side_menu.store_product_name()


@when('Confirm add to cart')
def add_item_to_cart(context):
    context.app.side_menu.confirm_add_to_cart()


@when('Navigate to Cart')
def search_results(context):
    context.app.side_menu.navigate_to_cart()


@then('Verify cart has correct product')
def verify_product_name(context):
    context.app.side_menu.verify_product_name()


@when('Hover favorites icon')
def hover_fav_icon(context):
    context.app.search_results.hover_fav_icon()


@then('Favorites tooltip is shown')
def verify_fav_tooltip(context):
    context.app.search_results.verify_fav_tooltip()


@then('Verify correct search results shown for {expected_text}')
def verify_search_results(context, expected_text):
    context.app.search_results.verify_search_results(expected_text)


@then('Verify {expected_text} in URL')
def verify_results_url(context, expected_text):
    context.app.search_results.verify_results_url(expected_text)

@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    # To see ALL listings (comment out if you only check top ones):
    # context.driver.execute_script("window.scrollBy(0,2000)", "")
    # sleep(2)
    # context.driver.execute_script("window.scrollBy(0,1000)", "")
    # sleep(2)

    products = context.driver.find_elements(*LISTINGS)[:8]  # [WebEl1, WebEl2, WebEl3, WebEl4]

    for product in products:
        title = product.find_element(*PRODUCT_TITLE).text
        assert title, 'Product title not shown'
        print(title)
        product.find_element(*PRODUCT_IMG)