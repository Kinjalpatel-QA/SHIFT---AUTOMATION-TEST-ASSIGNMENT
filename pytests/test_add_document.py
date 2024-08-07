from appium.webdriver.common.appiumby import AppiumBy
import time

# Importing login fixture
def test_add_document(login):
    driver = login

    driver.implicitly_wait(10)

    expected_doc_name = "Test Document"

    add_blank_document = driver.find_element(AppiumBy.XPATH, "//div[@id=':1i']/div/div/img[@src='https://ssl.gstatic.com/docs/templates/thumbnails/docs-blank-googlecolors.png']")
    add_blank_document.click()

    # time.sleep(2)

    # renaming blank document to Test Document.
    rename_document = driver.find_element(AppiumBy.XPATH, "//div[@id='docs-title-widget']/div/span[@id='docs-title-input-label-inner']")
    rename_document.send_keys(expected_doc_name)

    # After renaming , it will autosave to drive.

    # Verify document created with the same name/title.

    docs_home_page = driver.find_element(AppiumBy.XPATH, "//a[@data-tooltip='Docs home']/div[@id='docs-drive-logo']")
    docs_home_page.click()

    created_doc_name = driver.find_element(AppiumBy.XPATH, "//div[@role='listbox']/div/div/div/div[@class='docs-homescreen-grid-item-title']").text

    assert created_doc_name == expected_doc_name, "Document name did not match"
