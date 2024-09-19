from pages.base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):
    def open_page(self):
        self.browser.get(MainPageLocators.URL)

    def go_to_add_customer_page(self):
        self.browser.find_element(*MainPageLocators.Add_Customer).click()

    def go_to_customers_page(self):
        self.browser.find_element(*MainPageLocators.Customers).click()
