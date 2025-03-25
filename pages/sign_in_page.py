from selenium.webdriver.common.by import By
from pages.base_page import Page

class SignIn(Page):
    LOGIN_BUTTON = (By.CSS_SELECTOR, '#login')

    def verify_sign_in_open(self):
        self.wait_until_clickable(*self.LOGIN_BUTTON)