from selenium import webdriver
import time


class BasicAuthentication():
    def auth(self):
        driver = webdriver.Firefox(
            executable_path="E:\\Ismail\\Projects\\Automation_ISM\\Drivers\\geckodriver.exe")

        # protocol://username:password@url
        driver.get('https://admin:admin@the-internet.herokuapp.com/basic_auth')
        time.sleep(3)

        print(driver.title)

        driver.close()


test_obj = BasicAuthentication()
test_obj.auth()
