from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# Working with link text

class LinkText():

    def forgot_password(self):
        # Browser launch function
        # Step 1: launch the browser
        driver = webdriver.Firefox(
            executable_path="E:\\Ismail\\Projects\\Automation_ISM\\Drivers\\geckodriver.exe")

        # Step2 : Open Test URL
        driver.get("https://facebook.com")
        time.sleep(5)

        forgot_password = driver.find_element(By.LINK_TEXT, 'Forgotten password?')
        forgot_password.click()
        time.sleep(3)

        email = driver.find_element(By.ID, 'identify_email')
        email.send_keys('invalid@mail.com')
        time.sleep(2)

        search = driver.find_element(By.ID, 'did_submit')
        search.click()
        time.sleep(3)

        driver.close()


test_obj = LinkText()
test_obj.forgot_password()
