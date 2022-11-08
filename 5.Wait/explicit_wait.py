from selenium import webdriver
import time

from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class ExplicitWait():

    def explicit_wait(self):
        # Browser launch function
        # Step 1: launch the browser
        driver = webdriver.Firefox(
            executable_path="E:\\Ismail\\Projects\\Automation_ISM\\Drivers\\geckodriver.exe")

        # Step2 : Open Test URL
        driver.get("https://demo.opencart.com/index.php?route=account/login&language=en-gb")

        Login = driver.find_element(By.CSS_SELECTOR, '[action] h2')

        # ExplicitWait
        wait = WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException
                                                 ])
        print("Hello after ExplicitWait")

        print(Login.text)

        driver.close()


test_obj = ExplicitWait()
test_obj.explicit_wait()