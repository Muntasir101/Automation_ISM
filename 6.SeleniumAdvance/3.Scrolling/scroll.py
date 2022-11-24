from selenium import webdriver
import time
from selenium.webdriver.common.by import By


class Scroll():
    def scroll_page(self):
        driver = webdriver.Firefox(
            executable_path="E:\\Ismail\\Projects\\Automation_ISM\\Drivers\\geckodriver.exe")

        driver.get("https://www.bbc.com/")
        time.sleep(5)

        # To scroll down one page
        driver.execute_script("window.scrollBy(0, 15000)")
        time.sleep(5)

        # To scroll up one page
        driver.execute_script("window.scrollBy(0, -15000)")
        time.sleep(5)

        # Scroll to specific Element position
        asia_news = driver.find_element(By.LINK_TEXT, 'Asia News')
        driver.execute_script("arguments[0].scrollIntoView(true);", asia_news)
        time.sleep(3)

        driver.close()


test_obj = Scroll()
test_obj.scroll_page()
