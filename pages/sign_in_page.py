from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class SignIn(Page):
    LOGIN_BUTTON = (By.CSS_SELECTOR, '#login')
    TC_LINK = (By.CSS_SELECTOR, "[class*='sc-4'] [href*='terms-conditions']")
    EMAIL_FIELD = (By.CSS_SELECTOR, '#username')
    CONTINUE_BTTN = (By.CSS_SELECTOR, '#login')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#password')
    SIGNIN_BTTN = (By.CSS_SELECTOR, '#login')
    ERROR_MSG = (By.CSS_SELECTOR, '[data-test="authAlertDisplay"]')


    def open_sign_in_page(self):
        self.open_url('https://www.target.com/login')

    def click_tc_link(self):
        #target.com/login page not loading like in instructions. Workaround is to navigate directly to intended login page
        self.open_url(
            'https://www.target.com/login?client_id=ecom-web-1.0.0&ui_namespace=ui-default&back_button_action=browser&keep_me_signed_in=true&kmsi_default=false&actions=create_session_signin'
        )
        self.wait_until_clickable_click(*self.TC_LINK)

    def verify_sign_in_open(self):
        self.wait_until_clickable(*self.LOGIN_BUTTON)

    def enter_correct_email(self, email):
        self.find_element(*self.EMAIL_FIELD).send_keys(email)

    def click_continue(self):
        self.wait_until_clickable_click(*self.CONTINUE_BTTN)

    def enter_incorrect_password(self, password):
        self.find_element(*self.PASSWORD_FIELD).send_keys(password)

    def click_sign_in_button(self):
        self.find_element(*self.SIGNIN_BTTN).click()

    def verify_error_message(self):
        self.wait_until_visible(*self.ERROR_MSG)