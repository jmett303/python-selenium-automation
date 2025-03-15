# Amazon Logo, search by XPATH, "//i[@class='a-icon a-icon-logo']"
#
# Email field, search by ID, 'ap_email'
#
# Continue button, search by ID, 'continue'
#
# Conditions of use link, search by XPATH using text, "//a[text()='Conditions of Use']"
#
# Privacy Notice link, search by XPATH using text, "//a[text()='Privacy Notice']"
#
# Need help link, search by XPATH using partial text match, "//span[contains(text(), 'Need help?')]"
#
# Forgot your password link, search by ID, 'auth-fpp-link-bottom'
#
# Other issues with Sign-In link, search by ID, 'ap-other-signin-issues-link'
#
# Create your Amazon account button, search by ID, 'createAccountSubmit'

##################################################################################################################

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.target.com/')

# click sign in buttons
driver.find_element(By.XPATH, "//span[text()='Sign in']").click()
sleep(2)
driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()
sleep(2)

# verify results
expected_text = 'Sign into your Target account'
actual_text = driver.find_element(By.XPATH, "//h1[contains(@class, 'styles_ndsHeading__HcGpD')]").text
assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'
print('Test Case Passed')