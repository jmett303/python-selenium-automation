from selenium.webdriver.common.by import By
from pages.base_page import Page

class SideMenu(Page):
    SIDE_MENU_SIGN_IN = (By.CSS_SELECTOR, '[data-test="accountNav-signIn"]')

    def click_side_menu_sign_in(self):
        self.wait_until_clickable_click(*self.SIDE_MENU_SIGN_IN)


