from appium.webdriver.common.appiumby import AppiumBy


# Separating navigation part and test logic to maintain tests.
class ShiftLogin:
    def __init__(self, driver):
        self.driver = driver

    # Locators for login
    home_page_element = (AppiumBy.XPATH, "//div[@class='gb_yc']/div/a[@title='Gmail']")
    privacy_policy = (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@value='Privacy Policy and Terms of Use']")
    google_signin = (AppiumBy.XPATH, "//XCUIElementTypeButton[@title='Sign in with Google']")
    email_field = (AppiumBy.XPATH, "//input[@id='identifierId']")
    next_button = (AppiumBy.ACCESSIBILITY_ID, "Next")
    password_field = (AppiumBy.XPATH, "//input[@name='Passwd']")
    continue_button = (AppiumBy.XPATH, "//span[@class='VfPpkd-vQzf8d']")
    redirect_button = (AppiumBy.XPATH, "//div[@class='VfPpkd-RLmnJb']")
    access_checkbox = (AppiumBy.XPATH, "//input[@type='checkbox']")
    final_button = (AppiumBy.XPATH, "//div[@class='VfPpkd-RLmnJb']")

    def confirm_privacy_policy(self):
        self.driver.find_element(*self.privacy_policy).click()

    def select_google_signin(self):
        self.driver.find_element(*self.google_signin).click()

    def add_email(self, test_email):
        self.driver.find_element(*self.email_field).send_keys(test_email)

    def click_next_button(self):
        self.driver.find_element(*self.next_button).click()

    def add_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def another_next_button(self):
        self.driver.find_element(*self.continue_button).click()

    def click_continue_button(self):
        self.driver.find_element(*self.redirect_button).click()

    def give_access(self):
        self.driver.find_element(*self.access_checkbox).click()

    def click_final_button(self):
        self.driver.find_element(*self.final_button).click()
