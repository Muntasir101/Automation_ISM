from selenium import webdriver

class Chrome():
    def chrome_launch(self):
        driver = webdriver.Chrome(
            executable_path="/1.RunningTestOnVariousBrowsers/Drivers/chromedriver.exe")


obj = Chrome()
obj.chrome_launch()
