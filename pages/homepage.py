from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://demoblaze.com/index.html')

    def click_galaxy_s6(self):
        galaxy_s6 = self.browser.find_element(By.LINK_TEXT, value='Samsung galaxy s6')
        galaxy_s6.click()

    def click_monitor(self):
        monitor_link = self.browser.find_element(By.CSS_SELECTOR, value='''[onclick="byCat('monitor')"]''')
        monitor_link.click()


