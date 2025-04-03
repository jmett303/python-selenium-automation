from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class TermsAndConditionsPage(Page):
    def verify_tc_page_open(self):
        self.verify_partial_url('terms-conditions')