from selenium.webdriver.common.by import By
from pages.base_page import Page

class CartPage(Page):
    CART_EMPTY_TEXT = (By.CSS_SELECTOR, '[data-test="boxEmptyMsg"]')
    CART_ITEMS = (By.CSS_SELECTOR, '[data-test="cartItem"]')

    def verify_cart_is_empty(self):
        self.verify_text('Your cart is empty', *self.CART_EMPTY_TEXT)

    def verify_cart_page_opens(self):
        self.verify_url(f'{self.base_url}cart')   #references base_page.py

    def verify_item_added_to_cart(self):
        cart_items = self.find_elements(*self.CART_ITEMS)
        assert len(cart_items) == 1, f'Error. Expected 1 item in cart but got {len(cart_items)}'
        print(f'{len(cart_items)} item(s) in cart')