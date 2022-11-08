from selenium import webdriver
import time
from selenium.webdriver.common.by import By


class ImplicitWait():

    def implicit_wait(self):
        # Browser launch function
        # Step 1: launch the browser
        driver = webdriver.Firefox(
            executable_path="E:\\Ismail\\Projects\\Automation_ISM\\Drivers\\geckodriver.exe")

        # Step2 : Open Test URL
        driver.get("https://demo.opencart.com/index.php?route=account/login&language=en-gb")
        # ImplicitWait
        driver.implicitly_wait(100)

        Login = driver.find_element(By.CSS_SELECTOR, '[action] h22')
        # LoginVisibleText = Login.text
        print(Login.text)

        driver.close()


test_obj = ImplicitWait()
test_obj.implicit_wait()