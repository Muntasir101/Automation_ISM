from selenium import webdriver


class Browser_Commands():

    def command(self):
        # Browser launch function
        driver = webdriver.Firefox(
            executable_path="E:\\Ismail\\Projects\\Automation\\1.RunningTestOnVariousBrowsers\\Drivers\\geckodriver.exe")

        # Window maximize
        driver.maximize_window()

        # Website open function
        driver.get("https://google.com")

        # Browser close function
        driver.close()


obj = Browser_Commands()
obj.command()
