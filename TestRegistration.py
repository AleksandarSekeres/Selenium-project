import Constants
import Locators
import time
import MockedData
from selenium import webdriver

def TestRegistration(Username, Email, Password):
    driver= webdriver.Chrome()
    driver.get(Constants.BASE_URL)
    driver.maximize_window

    LoginButton= driver.find_element_by_css_selector(Locators.login_page_button_css_selector)
    LoginButton.click()

    RegistrationButton= driver.find_element_by_css_selector(Locators.login_page_register_button_css_selector)
    RegistrationButton.click()

    UsernameField= driver.find_element_by_css_selector(Locators.registration_page_username_css_selector)
    EmailField= driver.find_element_by_css_selector(Locators.registration_page_email_css_selector)
    PasswordField= driver.find_element_by_css_selector(Locators.registration_page_password_css_selector)
    PasswordOnceMoreField=driver.find_element_by_css_selector(Locators.registration_page_password_reapply_input_css_selector)
    RegistrationButton= driver.find_element_by_css_selector(Locators.registration_page_register_button_css_selector)

    UsernameField.send_keys(Username)
    EmailField.send_keys(Email)
    PasswordField.send_keys(Password)
    PasswordOnceMoreField.send_keys(Password)

    RegistrationButton.click()
    time.sleep(3)

    Registration= driver.find_element_by_css_selector(Locators.registration_page_ok_button_css_selector)

    if Registration.text== 'OK':
        print(f'successfull registration with {Username} , {Email} and {Password}')
    else:
        print(f'registration fail with {Username} , {Email} and {Password}')
    time.sleep(3)

TEST_DATA= MockedData.getTestData('MOCK_DATA.json')

for data in TEST_DATA:
    TestRegistration(data['Username'], data['Email'], data['Password'])