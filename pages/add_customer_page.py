import random

from data.data import AddCustomerData
from pages.locators import AddCustomerLocators
from pages.base_page import BasePage


class AddCustomerPage(BasePage):
    @staticmethod
    def generate_post_code(length=10):
        return "".join(random.choices("0123456789", k=length))

    @staticmethod
    def generate_first_name(post_code):
        numbers = [int(post_code[i:i + 2]) for i in range(0, len(post_code), 2)]

        first_name = ""
        for number in numbers:
            first_name += chr((number % 26) + ord("a"))

        return first_name

    def fill_in_first_name_field(self, text):
        self.browser.find_element(*AddCustomerLocators.FIRST_NAME).send_keys(text)

    def fill_in_last_name_field(self, text):
        self.browser.find_element(*AddCustomerLocators.LAST_NAME).send_keys(text)

    def fill_in_post_code_field(self, text):
        self.browser.find_element(*AddCustomerLocators.POST_CODE).send_keys(text)

    def add_customer(self):
        self.browser.find_element(*AddCustomerLocators.ADD_CUSTOMER).click()

    def should_be_alert(self):
        alert = self.browser.switch_to.alert
        alert_text = alert.text
        alert.accept()
        assert AddCustomerData.ALERT_TEXT in alert_text
