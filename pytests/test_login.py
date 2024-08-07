from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login(login):
    driver = login

    # After successful login , it will open your gmail inbox.
    # Asserting on homepage elements/gmail account elements to verify successful login.

    #  explicit_wait = WebDriverWait(driver, 10)
    # explicit_wait.until(EC.title_contains("Inbox"))

    driver.implicitly_wait(10)

    home_page_title = driver.title

    assert "Gmail" in home_page_title, "Login failed or taking longer to load home page."

    gmail_logo = driver.find_element(AppiumBy.XPATH, "//a[@title='Gmail']/img[@src='https://ssl.gstatic.com/ui/v1/icons/mail/rfr/logo_gmail_lockup_default_1x_r5.png']")

    assert gmail_logo.is_displayed(), "home page taking longer t load after login"
