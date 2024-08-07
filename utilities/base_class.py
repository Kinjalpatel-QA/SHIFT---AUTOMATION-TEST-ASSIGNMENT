from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest


@pytest.mark.usefixtures("appium_setup")
class BaseClass:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, driver, by, value, timeout=20):
        try:
            return WebDriverWait(driver, timeout).until(
                EC.visibility_of_element_located((by, value))
            )
        except Exception as e:
            print(f"Element not found: {e}")
            return None
