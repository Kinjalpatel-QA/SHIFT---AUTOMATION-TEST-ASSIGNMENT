from appium.webdriver.common.appiumby import AppiumBy
# from appium.webdriver import TouchAction
import time

from selenium.webdriver import ActionChains


def test_shift_version(login):
    driver = login

    driver.implicitly_wait(10)
    downloaded_shift_version = "9.3.3.1096"

    # Click on settings icon on top right header
    settings_icon = driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeButton[4]/XCUIElementTypeImage[@accessibilityId ='4F8CBDA2-A2E5-42C2-9B8D-2CFE37B437B3']")
    settings_icon.click()

    '''Clicking on advance settings require to scroll the settings side window.
     As selenium supports execute_script/scrollBy for web , for desktop app , performing scroll down using TouchAction class
     using x, y coordinates from start and end point. we can locate coordinates inside accessibility inspector.'''

    # TouchAction class is not supported in latest appium-python-client version (4.0.1). so using ActionChains class
    # scroll = TouchAction(driver)

    scroll = ActionChains(driver)

    start_x = 188
    start_y = 166
    end_y = 755

    # Scrolling vertically on page so x remain same
    # scroll.press(x=start_x, y=start_y).move_to(x=start_x, y=end_y).release().perform()

    scroll.move_by_offset(start_x, start_y).click_and_hold().move_by_offset(0, end_y - start_y).release().perform()

    # time.sleep(2)

    advanced_settings = driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeGroup[10]/XCUIElementTypeButton[@title='Advanced Settings']")
    advanced_settings.click()

    # time.sleep(2)

    # Inside settings page , shift version is located under shadow root.
    # Locating & handling shadow host and shadow root elements using execute_script method.

    shadow_host = driver.find_element(AppiumBy.ID, "main")

    shadow_root = driver.execute_script('return arguments[0].shadowRoot', shadow_host)

    installed_shift_version = shadow_root.find_element(AppiumBy.XPATH, "//dl/div/dd").text

    print("installed version:", installed_shift_version)

    if installed_shift_version == downloaded_shift_version:

        print("Correct Version installed")

    else:

        print("Shift versions did not match")
