

import pytest
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.options.mac import Mac2Options
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
from selenium import webdriver

from page_objects.shift_login import ShiftLogin
from utilities.base_class import BaseClass

# Initialize appium server to start and declaring desired capabilities as caps
@pytest.fixture(scope="module")
def appium_setup():
    caps = {
        'platformName': 'mac',
        'appium:automationName': 'Mac2',
        'appium:app': '/Applications/Shift.app',
        'appium:serverStartupTimeout': 300000
    }

    # Starting appium server on 4725 port (as got error on default port 4723)
    appium_server_url = "http://127.0.0.1:4725"

    # We can also start appium server inside test
    '''appium_service = AppiumService()
     appium_service.start() '''

    options = AppiumOptions()
    options.load_capabilities(caps)

    driver = webdriver.Remote(command_executor=appium_server_url,
                              options=options)

    yield driver
    driver.quit()
    # appium_service.stop()

# Declaring login into shift as fixture so can be easily used in other tests.
# Also using appium_setup fixture to start the server before login and baseclass from utilities.
# Importing ShiftLogin class from page_objects.
@pytest.fixture(scope="module")
def login(appium_setup):
    driver = appium_setup
    shift_login = ShiftLogin(driver)
    base = BaseClass(driver)
    test_email = "test.shiftbrowser@gmail.com"
    password = "uniquebrowser"

    shift_home_page = base.wait_for_element(driver, *shift_login.home_page_element, timeout=5)
    if not shift_home_page:
        try:
            # Privacy check
            assert base.wait_for_element(driver, *shift_login.privacy_policy), "Privacy policy checkbox not found"
            shift_login.confirm_privacy_policy()

            # Google Sign-in
            assert base.wait_for_element(driver, *shift_login.google_signin), "Google Sign-in button not found"
            shift_login.select_google_signin()

            # Email field
            assert base.wait_for_element(driver, *shift_login.email_field), "Email field not found"
            shift_login.add_email(test_email)

            # Next button
            assert base.wait_for_element(driver, *shift_login.next_button), "Next button not found"
            shift_login.click_next_button()

            # Password field
            assert base.wait_for_element(driver, *shift_login.password_field), "Password field not found"
            shift_login.add_password(password)

            # Another next button
            assert base.wait_for_element(driver, *shift_login.continue_button), "Password page next button not found"
            shift_login.another_next_button()

            # Continue button
            assert base.wait_for_element(driver, *shift_login.redirect_button), "Continue button not found"
            shift_login.click_continue_button()

            # Checkbox to give access
            assert base.wait_for_element(driver, *shift_login.access_checkbox), "Access checkbox not found"
            shift_login.give_access()

            # Final continue button
            assert base.wait_for_element(driver, *shift_login.final_button), "Final continue button not found"
            shift_login.click_final_button()

            print("Login completed successfully.")
        except Exception as e:
            print(f"Test failed: {e}")

    yield driver

# Using ChromeOptions class to download Shift app from chrome.
@pytest.fixture(scope='module')
def chrome_driver():
    options = webdriver.ChromeOptions()

    # Setting download preferences
    prefs = {"download.default_directory": "/Users/kinjal/Downloads",
             "profile.default_content_setting_values.automatic_downloads": 1,
             "download.prompt_for_download": False,
             "safebrowsing.enabled": False,

             }
    options.add_experimental_option("prefs", prefs)

    # disabling some chrome features that can block download
    options.add_argument("--unsafely-treat-insecure-origin-as-secure=https://shift.com/download/")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-extensions")
    options.add_argument("--headless")
    options.add_argument("--ignore-certificate-errors")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
