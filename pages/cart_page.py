from selenium.webdriver.common.by import By
from pages.base_page import Page

class CartPage(Page):
    CART_EMPTY_TEXT = (By.CSS_SELECTOR, '[data-test="boxEmptyMsg"]')

    def verify_cart_is_empty(self):
        expected_result = 'Your cart is empty'
        actual_result = self.driver.find_element(*self.CART_EMPTY_TEXT).text
        assert expected_result == actual_result, f'Error. Text {expected_result} not in {actual_result}'
