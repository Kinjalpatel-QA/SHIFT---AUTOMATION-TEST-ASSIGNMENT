### SHIFT AUTOMATION TECHNICAL CHALLENGE

This repository contains the automation test scripts for the Shift application using Appium with Mac2Driver on macOS.


# Prerequisites

1. macOS - (version 13.4 or later recommended)
2. Python - ( I have used python 3.12.2) : download and install or using brew on terminal pass `brew install python`
3. Appium - (I have used 2.11.2): after node.js installation , use command : `npm install -g appium`
4. Node.js and npm (for Appium installation) - download and install node.js or use command : `brew install node`, npm version >= 8 required.(I have used node v21.5.0 , and npm 10.2.4)
5. IDE - PyCharm preferred
6. Xcode (for accessibility settings) - download xcode compatible version to your macOS version from app store/apple developer website for specific version.( I have used 14.1) 
7. Mac2driver - As Shift is a desktop application , I have used appium's Mac2driver to automate app on mac device.( similar to WinAppDriver for windows).
                use command : `appium driver install mac2`
8. Selenium - I have used it for first `test_shift_download.py` and chrome_Driver fixture as to interect with web page and automate downloading of shift app.
              use command : `pip3 install selenium` ( I have used 4.23.1)
9. Appium-python-client - As I have created scripts using appium-python , appium-python-client is a Python library that allows to interact with Appium servers.
              use command : pip3 install Appium-Python-Client ( I have used 4.0.1)
10. pytest - I have used pytest testing framework for writing/managing test scripts. use command : pip3 install pytest ( I have used 8.3.2)
             or we can also add these last 3 from the PyCharm->Settings->project-> set your python interpreter and install required packages by clicking + button.
11.  Git -  push/pull test files.
12.  Accessibility Settings - as Mac driver relies on accessibility to get control over the entire desktop, we need to grant accessibility permission to following :

      - Xcode : You can find in Applications.
      - Xcode Helper : you can find it in "/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/Library/Xcode/Agents/"
      - Appium : `where appium` will give you location on your device , navigate to appium file which has no extention and drag and drop to system settings.
      - Mac2Driver : `npm list -g appium-mac2-driver` use this command to find the location of driver , navigate to that location to drag and drop folder.
      - Terminal : You can find in "Applications/Utilities"
      - PyCharm : You can find in Applications.

  Click apple logo -> system settings -> privacy & security -> accessibity -> drag and drop each of above to enable permission.
  ( If you have full disk access , you can also enable there too )

13.  Chrome browser - To navigate to shift download page.
14.  Chrome Browser Settings -  disable following settings that can block automatic download.

        - Chrome->settings->privacy & security-> site settings->additional permissions -> automatic downloads -> disable "Don't allow sites to automatically download multiple files".
        - Add shift web path to the list of "Allowed to automatically download multiple files"
        - disable safe browsing from Chrome->settings->privacy & security-> security-> safe browsing.
15. Additional device settings -  disable any firewall and select allow app to download from "app store and identified developers".
16. Set the Active Xcode developer directory -  use command on terminal : `sudo xcode-select -s /Applications/Xcode.app/Contents/Developer`


# Starting & Running Project On you Mac device

1. Clone this repository to your device.
2. open project in Pycharm IDE.
3. On terminal-> cd project folder path.
4. After finishing all prerequisites , start appium server using this command : `appium --address 127.0.0.1 --port 4725`
5. Open another terminal tab,cd project-> pytests. Then run the tests using command : `pytest -v -s`
6. To create html report , first install ` pip install pytest-html` and then run : `pytest -v -s --html=report.html`

# Additional Info

1. Make sure you have the Shift application installed at /Applications/Shift.app
