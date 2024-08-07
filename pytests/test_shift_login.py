import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy

from page_objects.shift_login import ShiftLogin


# I have created login test separately first using base calss in same test , so keeping this test just for comparision in structure.
class BaseClass:
    def wait_for_element(self, driver, by, value, timeout=20):
        WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((by, value)))


class TestShiftLogin(BaseClass):

    def test_shift_login(self, appium_setup):
        driver = appium_setup

        shift_login = ShiftLogin(driver)

        try:
            # Privacy check
            assert self.wait_for_element(driver, *shift_login.privacy_policy), "Privacy policy checkbox not found"
            shift_login.confirm_privacy_policy()

            # Google Sign-in
            assert self.wait_for_element(driver, *shift_login.google_signin), "Google Sign-in button not found"
            shift_login.select_google_signin()

            # Email field
            assert self.wait_for_element(driver, *shift_login.email_field), "Email field not found"
            shift_login.add_email("test.shiftbrowser@gmail.com")

            # Next button
            assert self.wait_for_element(driver, *shift_login.next_button), "Next button not found"
            shift_login.click_next_button()

            # Password field
            assert self.wait_for_element(driver, *shift_login.password_field), "Password field not found"
            shift_login.add_password("uniquebrowser")

            # Another next button
            assert self.wait_for_element(driver, *shift_login.continue_button), "Password page next button not found"
            shift_login.another_next_button()

            # Continue button
            assert self.wait_for_element(driver, *shift_login.redirect_button), "Continue button not found"
            shift_login.click_continue_button()

            # Checkbox to give access
            assert self.wait_for_element(driver, *shift_login.access_checkbox), "Access checkbox not found"
            shift_login.give_access()

            # Final continue button
            assert self.wait_for_element(driver, *shift_login.final_button), "Final continue button not found"
            shift_login.click_final_button()

            print("Login completed successfully.")

        except Exception as e:
            print(f"Test failed: {e}")
