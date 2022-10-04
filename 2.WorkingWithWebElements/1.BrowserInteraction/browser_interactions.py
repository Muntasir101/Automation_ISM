from selenium import webdriver
import time


class BrowserInteraction():
    def all_commands(self):
        # Browser launch function
        driver = webdriver.Firefox(
            executable_path="E:\\Ismail\\Projects\\Automation\\1.RunningTestOnVariousBrowsers\\Drivers\\geckodriver.exe")

        # Window maximize
        driver.maximize_window()

        # Website open function
        driver.get("https://apple.com")
        time.sleep(2)

        # get Title
        title = driver.title
        #print(title)

        page_source = driver.page_source
        # print(page_source)

        # Website open function
        driver.get("https://google.com")
        time.sleep(3)

        # Get URL from the page
        url = driver.current_url
        # print(url)

        # Goes one step backward in the browser history.back to previous page : Apple
        driver.back()
        time.sleep(2)
        print('Back to:' + driver.title)

        # Goes one step forward in the browser history.Forward to : Google.com
        driver.forward()
        time.sleep(2)
        print("Forward to:" + driver.title)

        # Refreshes the current page.
        driver.refresh()

        # Browser close function
        driver.close()


test_obj = BrowserInteraction()
test_obj.all_commands()
