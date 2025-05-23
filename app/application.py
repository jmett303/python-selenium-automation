from pages.base_page import Page
from pages.cart_page import CartPage
from pages.header import Header
from pages.help_page import HelpPage
from pages.search_results_page import SearchResultsPage
from pages.main_page import MainPage
from pages.side_menu_page import SideMenu
from pages.sign_in_page import SignIn
from pages.target_app_page import TargetAppPage
from pages.t_and_c_page import TermsAndConditionsPage


class Application:
    def __init__(self, driver):
        self.driver = driver
        self.base_page = Page(driver)
        self.cart_page = CartPage(driver)
        self.header = Header(driver)
        self.help_page = HelpPage(driver)
        self.main_page = MainPage(driver)
        self.search_results = SearchResultsPage(driver)
        self.side_menu = SideMenu(driver)
        self.sign_in_page = SignIn(driver)
        self.t_and_c_page = TermsAndConditionsPage(driver)
        self.target_app_page = TargetAppPage(driver)