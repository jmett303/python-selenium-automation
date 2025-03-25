from selenium.webdriver.common.by import By
from pages.base_page import Page


class SideMenu(Page):
    SIDE_MENU_SIGN_IN = (By.CSS_SELECTOR, '[data-test="accountNav-signIn"]')
    PRODUCT_NAME = (By.CSS_SELECTOR, '[data-test="content-wrapper"] h4')
    PRODUCT_NAME_IN_CART = (By.CSS_SELECTOR, '[data-test="cartItem-title"]')
    ADD_TO_CART_2 = (By.CSS_SELECTOR, '[data-test="orderPickupButton"]')
    VIEW_CART = (By.CSS_SELECTOR, '[href="/cart"]')

    def click_side_menu_sign_in(self):
        self.wait_until_clickable_click(*self.SIDE_MENU_SIGN_IN)

    def store_product_name(self):
        self.wait_until_visible(*self.PRODUCT_NAME)
        self.product_name = self.find_element(*self.PRODUCT_NAME).text
        print('Product name stored: ', self.product_name)

    def confirm_add_to_cart(self):
        self.wait_until_clickable_click(*self.ADD_TO_CART_2)

    def navigate_to_cart(self):
        self.wait_until_clickable_click(*self.VIEW_CART)

    def verify_product_name(self):
        self.wait_until_visible(*self.PRODUCT_NAME_IN_CART)
        self.product_name_in_cart = self.find_element(*self.PRODUCT_NAME_IN_CART).text
        assert self.product_name_in_cart[:20] == self.product_name[:20], \
            f'Error. Expected {self.product_name} but got {self.product_name_in_cart}'
