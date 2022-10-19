from selenium import webdriver
import time
from selenium.webdriver.common.by import By


class GetText():

    def text_element(self):
        # Browser launch function
        # Step 1: launch the browser
        driver = webdriver.Firefox(
            executable_path="E:\\Ismail\\Projects\\Automation_ISM\\Drivers\\geckodriver.exe")

        # Step2 : Open Test URL
        driver.get("https://demo.opencart.com/index.php?route=account/login&language=en-gb")
        time.sleep(5)

        Login = driver.find_element(By.CSS_SELECTOR, '[action] h2')
        # LoginVisibleText = Login.text
        print(Login.text)

        driver.close()


test_obj = GetText()
test_obj.text_element()
