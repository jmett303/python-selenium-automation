from selenium.webdriver.common.by import By
from pages.base_page import Page

class HeaderPage(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BUTTON = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")

    def search(self):
        self.input_text('tea', *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BUTTON)