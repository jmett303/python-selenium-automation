from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class SearchResultsPage(Page):
    SEARCH_RESULTS_TEXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")
    ADD_TO_CART = (By.CSS_SELECTOR, '[index="0"] [id*="addToCart"]')
    FAVORITES_BTN = (By.CSS_SELECTOR, "[data-test='FavoritesButton']")
    FAVORITES_TOOLTIP_TXT = (By.XPATH, "//*[text()='Click to sign in and save']")

    def hover_fav_icon(self):
        self.hover_element(*self.FAVORITES_BTN)

    def verify_fav_tooltip(self):
        self.wait_until_visible(*self.FAVORITES_TOOLTIP_TXT)

    def verify_search_results(self, expected_text):
        self.verify_partial_text(expected_text, *self.SEARCH_RESULTS_TEXT)

    def verify_results_url(self, expected_partial_url):
        self.verify_partial_url(expected_partial_url)

    def add_item_to_cart(self):
        sleep(8)
        self.wait_until_clickable_click(*self.ADD_TO_CART)

