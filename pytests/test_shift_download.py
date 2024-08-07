import pytest
import time
import os.path
from selenium.webdriver.common.by import By


def test_shift_download(chrome_driver):
    driver = chrome_driver
    download_path = '/Users/kinjal/Downloads'
    shift_version = 'shift-v9.3.3.1096-stable-arm64.dmg'
    shift_path = os.path.join(download_path, shift_version)

    driver.get("https://shift.com/download/")

    driver.implicitly_wait(10)
    print("Navigated to Shift download page.")
    try:
        download_link = driver.find_element(By.LINK_TEXT, "Apple Silicon")
        download_link.click()
        print("Clicked on the download link.")

    except Exception as e:
        print(f"Failed to find or click the download link: {e}")

    shift_successful = False
    # time.sleep(10)
    if os.path.exists(shift_path):
        shift_successful = True
        print("yes , File download is Successful")
    else:
        print("File download is not Successful")

    assert shift_successful, "File download is not Successful"
