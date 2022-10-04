from selenium import webdriver


class Firefox():
    def firefox_launch(self):
        driver = webdriver.Firefox(
            executable_path="E:\\Ismail\\Projects\\Automation\\1.RunningTestOnVariousBrowsers\\Drivers\\geckodriver.exe")


obj = Firefox()
obj.firefox_launch()