from pages.base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):
    def go_to_add_customer_page(self):
        locator = MainPageLocators.ADD_CUSTOMER
        self.wait_to_element_visible(locator)
        self.browser.find_element(*locator).click()

    def go_to_customers_page(self):
        locator = MainPageLocators.CUSTOMERS
        self.wait_to_element_visible(locator)
        self.browser.find_element(*locator).click()
