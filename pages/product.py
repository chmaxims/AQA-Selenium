from selenium.webdriver.common.by import By

class ProductPage:
    def __init__(self, browser):
        self.browser = browser

    def check_title_is(self, title):
        page_title = self.browser.find_element(By.CSS_SELECTOR, value='h2')
        assert page_title.text == title
    def check_products_count(self, count):
        monitors = self.browser.find_elements(By.CSS_SELECTOR, value='.card')
        assert len(monitors) == count, f"Длина списка: {len(monitors)}, ожидается {count}"