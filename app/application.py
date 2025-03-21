from pages.base_page import Page
from pages.cart_page import CartPage
from pages.header import Header
from pages.search_results_page import SearchResultsPage
from pages.main_page import MainPage

class Application:
    def __init__(self, driver):
        self.driver = driver
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.search_results = SearchResultsPage(driver)
        self.cart_page = CartPage(driver)

