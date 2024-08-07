from appium.webdriver.common.appiumby import AppiumBy
import time


def test_google_app(login):
    driver = login
    expected_app = "Docs"

    driver.implicitly_wait(10)
    # Click + button on bottom left to select/add google docs application
    add_button = driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeButton[@label='Add to Shift']")
    add_button.click()

    add_application = driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeStaticText[@value='Add Application']")
    add_application.click()

    # We can either select category (here Google) from left sidebar
    '''select_category = driver.find_element(AppiumBy.XPATH,"//div[@class='sidebar-nav-item-category' and text()='Google']")
    select_category.click()'''

    # Or can search for the app name directly in search field.
    search_field = driver.find_element(AppiumBy.XPATH, "//input[@name='app-search']")
    search_field.send_keys("google docs")

    # Click/select google app from search results
    select_google_docs = driver.find_element(AppiumBy.XPATH,"//div[@class='app-grid filtered-apps']/div/div/div[@text='Google Docs']")
    select_google_docs.click()

    # Add account name for app.
    add_account_name = driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeTextField[@title='Account name']")
    add_account_name.send_keys("Test Account")

    # As you logged in using your test email , it shows test email selected already in dropdown.
    # If you select any workspace created , then have to add steps for login using your gmail.

    # Save docs app
    save_selected_app = driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeButton[@title='Save']")
    save_selected_app.click()

    # time.sleep(2)

    # verify Google Docs app added successfully or not

    actual_app = driver.find_element(AppiumBy.XPATH, "//div[@class='gb_yc']/div/a[@aria-label='Docs']/span").text

    assert expected_app == actual_app, "The app added is not Google Docs"
