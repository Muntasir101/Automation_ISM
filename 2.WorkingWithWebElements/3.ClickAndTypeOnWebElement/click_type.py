from selenium import webdriver
import time
from selenium.webdriver.common.by import By


class ClickAndType():

    def login_tc_001(self):
        # Browser launch function
        # Step 1: launch the browser
        driver = webdriver.Firefox(
            executable_path="E:\\Ismail\\Projects\\Automation_ISM\\Drivers\\geckodriver.exe")

        # Step2 : Open Test URL
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)

        # find_element : Find an element given a By strategy and locator.
        # send_keys: Simulates typing into the element.

        # Step 3: Finding Username
        username = driver.find_element(By.NAME, 'username')

        # Step 4: Typing on the Username Field
        username.send_keys('Admin')
        time.sleep(2)

        # Step 5: Finding  Password
        password = driver.find_element(By.NAME, 'password')

        # Step 6: Typing on the Password Field
        password.send_keys('admin123')
        time.sleep(2)

        # Step 7: Finding Login Button
        login_button = driver.find_element(By.XPATH,
                                           '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')

        # Step 8: Click on the Login Button
        login_button.click()
        time.sleep(5)

        # Step 9: Close the Browser
        driver.close()


test_obj = ClickAndType()
test_obj.login_tc_001()
