from pages.base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):
    def go_to_add_customer_page(self):
        self.browser.find_element(*MainPageLocators.ADD_CUSTOMER).click()

    def go_to_customers_page(self):
        self.browser.find_element(*MainPageLocators.CUSTOMERS).click()
