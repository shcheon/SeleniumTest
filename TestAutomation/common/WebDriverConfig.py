from selenium import webdriver

class ChromeWebDriver:
    def __init__(self, mode=''):
        self.driver_file_path = "./driver/chromedriver.exe"
        self.mode = mode

        if self.mode.lower() == "headless":
            self.options = webdriver.ChromeOptions()
            self.options.add_argument('headless')
            self.options.add_argument("disable-gpu")
            self.driver = webdriver.Chrome(self.driver_file_path, chrome_options=self.options)
        else:
            self.options = webdriver.ChromeOptions()
            self.options.add_argument('window-size=1920x1080')

