from selenium import webdriver
import time
from selenium.webdriver.common.by import By


class WebElementState():

    def element_enable_check(self):
        # Browser launch function
        # Step 1: launch the browser
        driver = webdriver.Firefox(
            executable_path="E:\\Ismail\\Projects\\Automation_ISM\\Drivers\\geckodriver.exe")

        # Step2 : Open Test URL
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)

        # Step 3: Finding Username
        username = driver.find_element(By.NAME, 'username')

        # is_enabled: Returns whether the element is enabled.If not, returns False
        enable_check = username.is_enabled()
        print("Username Enable Status: " + str(enable_check))

        # Close the Browser
        driver.close()

    def element_display_check(self):
        # Browser launch function
        # Step 1: launch the browser
        driver = webdriver.Firefox(
            executable_path="E:\\Ismail\\Projects\\Automation_ISM\\Drivers\\geckodriver.exe")

        # Step2 : Open Test URL
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)

        # Step 3: Finding Username
        username = driver.find_element(By.NAME, 'username')

        # is_displayed: Whether the element is visible to a user.If not, returns False
        display_check = username.is_displayed()
        print("Username Display Status: " + str(display_check))

        # Close the Browser
        driver.close()


test_obj = WebElementState()
#test_obj.element_enable_check()
test_obj.element_display_check()
