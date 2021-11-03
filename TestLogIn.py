import MockedData
from selenium import webdriver
import Constants
import Locators
import time

def TestLogIn(Email, Password):
    driver= webdriver.Chrome()
    driver.get(Constants.BASE_URL)
    driver.maximize_window

    Login= driver.find_element_by_css_selector(Locators.login_page_button_css_selector)
    Login.click()

    EmailField= driver.find_element_by_css_selector(Locators.login_page_email_css_selector)
    PasswordField= driver.find_element_by_css_selector(Locators.login_page_password_css_selector)
    EmailField.send_keys(Email)
    PasswordField.send_keys(Password)

    Button= driver.find_element_by_css_selector(Locators.login_page_login_button_css_selector)
    Button.click()

    if (driver.current_url== f'{Constants.BASE_URL}'):
        print(f'Login successful with {Email} and {Password}')
    else:
        print(f'login unseccessful with{Email} and {Password}')
    
    time.sleep(3)

TEST_DATA= MockedData.getTestData('MOCK_DATA.json')

for data in TEST_DATA:
    TestLogIn(data['Email'], data['Password'])