from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Dropdown():
    def dropdown(self):
        driver = webdriver.Firefox(
            executable_path="E:\\Ismail\\Projects\\Automation_ISM\\Drivers\\geckodriver.exe")

        driver.get("https://the-internet.herokuapp.com/dropdown")
        time.sleep(5)

        dropdown_list = driver.find_element(By.ID, 'dropdown')
        sel = Select(dropdown_list)
        #sel.select_by_visible_text('Option 1')
        #sel.select_by_value("2")
        sel.select_by_index(1)
        time.sleep(3)

        driver.close()

        driver.find_elements(By.ID, 'dropdown')


test_obj = Dropdown()
test_obj.dropdown()
