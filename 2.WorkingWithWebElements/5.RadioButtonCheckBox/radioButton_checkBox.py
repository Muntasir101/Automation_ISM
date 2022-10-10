from selenium import webdriver
import time
from selenium.webdriver.common.by import By


class RadioCheckBox():
    def radio_checkbox(self):
        driver = webdriver.Firefox(
            executable_path="E:\\Ismail\\Projects\\Automation_ISM\\Drivers\\geckodriver.exe")

        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)

        # Login
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
                                           '//*[@id="app"]/div[1]/div/div[1]/div/'
                                           'div[2]/div[2]/form/div[3]/button')

        # Step 8: Click on the Login Button
        login_button.click()
        time.sleep(5)

        # Go to My Info Module
        MyInfo = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside'
                                               '/nav/div[2]/ul/li[6]/a/span')
        MyInfo.click()
        time.sleep(3)

        # Gender Female: Radio Button
        Gender_female = driver.find_element(By.CSS_SELECTOR,
                                            '#app > div.oxd-layout > div.oxd-layout-container > '
                                            'div.oxd-layout-context > div > div > div > '
                                            'div.orangehrm-edit-employee-content > '
                                            'div.orangehrm-horizontal-padding.orangehrm-vertical-padding > form > '
                                            'div:nth-child(5) > div:nth-child(2) > div:nth-child(2) > div > '
                                            'div.--gender-grouped-field > div:nth-child(2) > div:nth-child(2) > div > '
                                            'label > span')
        Gender_female.click()
        time.sleep(2)

        Smoker = driver.find_element(By.XPATH,
                                     'div.oxd-form-row:nth-child(7) > div:nth-child(1) > div:nth-child(2) > '
                                     'div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > label:nth-child(1) > '
                                     'span:nth-child(2) > i:nth-child(1)')
        Smoker.click()
        time.sleep(2)

        driver.close()


test_obj = RadioCheckBox()
test_obj.radio_checkbox()
