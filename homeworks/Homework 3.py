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
driver.get('https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3F_encoding%3DUTF8%26ref_%3Dnav_custrec_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')
sleep(5)

#Optimal locators for Create Account on amazon.com

#Amazon logo
driver.find_element(By.CSS_SELECTOR, '.a-link-nav-icon .a-icon')
#"Create Account"
driver.find_element(By.CSS_SELECTOR, '.a-box-inner h1')
#"Your Name"
driver.find_element(By.CSS_SELECTOR, '#ap_customer_name')
#Email
driver.find_element(By.CSS_SELECTOR, "[type='email']")
#Password
driver.find_element(By.CSS_SELECTOR, '#ap_password')
#"Passwords must be at least 6 characters"
driver.find_element(By.CSS_SELECTOR, '[id*=requirement] .a-alert-content')
#"Re-enter password" field
driver.find_element(By.CSS_SELECTOR, '#ap_password_check')
#"Create your amazon account" button
driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
#Conditions of Use hyperlink
driver.find_element(By.CSS_SELECTOR, '#legalTextRow [href*=condition]')
#Privacy notice hyperlink
driver.find_element(By.CSS_SELECTOR, '#legalTextRow [href*=privacy]')
#Sign in hyperlink
driver.find_element(By.CSS_SELECTOR, '.a-link-emphasis')


