from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open_page(self):
        self.browser.get(self.url)

    def wait_to_element_visible(self, locator, timeout=10):
        WebDriverWait(self.browser, timeout).until(ec.visibility_of_element_located(locator))
