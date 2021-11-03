import MockedData
from selenium import webdriver
import Constants
import Locators
import time

def LogOutTest(Email, Password):
    driver= webdriver.Chrome()
    driver.get(Constants.BASE_URL)
    driver.maximize_window
    time.sleep(3)
    Login= driver.find_element_by_css_selector(Locators.login_page_button_css_selector)
    Login.click()

    EmailField= driver.find_element_by_css_selector(Locators.login_page_email_css_selector)
    PasswordField= driver.find_element_by_css_selector(Locators.login_page_password_css_selector)
    EmailField.send_keys(Email)
    PasswordField.send_keys(Password)
    Button= driver.find_element_by_css_selector(Locators.login_page_login_button_css_selector)
    Button.click()
    time.sleep(3)



    logout= driver.find_element_by_css_selector(Locators.logout_page_logout_button_css_selector)
    logout.click()
    time.sleep(1)

    if (driver.current_url == f'{Constants.BASE_URL}'):
        print(f'Logout Successfull with{Email} and {Password}')
    else:
        print(f'Logout failed with {Email} and {Password}!')
    time.sleep(3)

TEST_DATA= MockedData.getTestData('MOCK_DATA.json')

for data in TEST_DATA:
    LogOutTest(data['Email'], data['Password'])