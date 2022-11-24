from selenium import webdriver
import time
from selenium.webdriver.common.by import By


class Alert():
    def alert_handle(self):
        driver = webdriver.Firefox(
            executable_path="E:\\Ismail\\Projects\\Automation_ISM\\Drivers\\geckodriver.exe")

        driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        time.sleep(5)

        # Open normal Alert
        normal_alert = driver.find_element(By.CSS_SELECTOR, 'li:nth-of-type(1) > button')
        normal_alert.click()
        driver.implicitly_wait(10)

        # Get Text/Title from Alert
        normal_alert_text = driver.switch_to.alert.text
        print(normal_alert_text)

        # Click OK on Alert
        driver.switch_to.alert.accept()
        time.sleep(3)

        # Open confirm Alert
        confirm_alert = driver.find_element(By.CSS_SELECTOR, 'li:nth-of-type(2) > button')
        confirm_alert.click()

        # Get Text/Title from Alert
        confirm_alert_text = driver.switch_to.alert.text
        print(confirm_alert_text)

        # Click Cancel on Alert
        driver.switch_to.alert.dismiss()

        # Open prompt Alert
        prompt_alert = driver.find_element(By.CSS_SELECTOR, 'li:nth-of-type(3) > button')
        prompt_alert.click()

        # Get Text/Title from Alert
        prompt_alert_text = driver.switch_to.alert.text
        print(prompt_alert_text)

        # Type something on the alert
        driver.switch_to.alert.send_keys('Test Automation')
        time.sleep(3)

        # Click OK on Alert
        driver.switch_to.alert.accept()

        driver.close()


test_obj = Alert()
test_obj.alert_handle()
