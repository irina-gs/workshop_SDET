class BasePage:
    def __init__(self, browser, timeout=5):
        self.browser = browser
        self.browser.implicitly_wait(timeout)
