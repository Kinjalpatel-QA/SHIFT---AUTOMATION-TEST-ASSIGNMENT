from appium.webdriver.common.appiumby import AppiumBy
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_workspace(login):
    driver = login

    driver.implicitly_wait(10)
    # time.sleep(10)
    added_workspace_name = "TestWorkspace"

    wait = WebDriverWait(driver, 20)
    add_button = wait.until(
        EC.element_to_be_clickable((AppiumBy.XPATH, "//XCUIElementTypeButton[@label='Add to Shift']")))

    # Locate and click the "+" button
    # add_button = driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeButton[@label='Add to Shift']")
    add_button.click()

    add_workspace = driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeStaticText[@value='Add Workspace']")
    add_workspace.click()

    # Add workspace name
    workspace_name_field = driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeTextField[@title='Workspace name']")
    workspace_name_field.send_keys(added_workspace_name)

    create_workspace = driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeButton[@title='Create Workspace']")
    create_workspace.click()

    # time.sleep(2)
    # We can also use ActionChains class to perform mouse events like hover over element.
    '''action = ActionChains(driver)
    action.move_to_element(driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeMenu/XCUIElementTypeMenuItem[@title='TestWorkspace']")).perform()'''

    actual_workspace_name = driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeMenu/XCUIElementTypeMenuItem[@title='TestWorkspace']").text

    assert actual_workspace_name == added_workspace_name, "workspace names did not match"

