from selenium.webdriver.common.by import By
from pages.base_page import Page

class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BUTTON = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    SIGN_IN = (By.CSS_SELECTOR, '[data-test="@web/AccountLink"]')

    def search(self, text):
        print(f'Searching for {text}')
        self.input_text(text, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BUTTON)

    def click_sign_in(self):
        self.wait_until_clickable_click(*self.SIGN_IN)