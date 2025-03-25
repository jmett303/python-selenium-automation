from pages.base_page import Page
from pages.cart_page import CartPage
from pages.header import Header
from pages.search_results_page import SearchResultsPage
from pages.main_page import MainPage
from pages.side_menu_page import SideMenu
from pages.sign_in_page import SignIn


class Application:
    def __init__(self, driver):
        self.cart_page = CartPage(driver)
        self.driver = driver
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.search_results = SearchResultsPage(driver)
        self.side_menu = SideMenu(driver)
        self.sign_in = SignIn(driver)