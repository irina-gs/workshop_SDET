import random

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
        input_first_name = self.browser.find_element(*AddCustomerLocators.First_Name)
        input_first_name.send_keys(text)

    def fill_in_last_name_field(self, text):
        input_last_name = self.browser.find_element(*AddCustomerLocators.Last_Name)
        input_last_name.send_keys(text)

    def fill_in_post_code_field(self, text):
        input_post_code = self.browser.find_element(*AddCustomerLocators.Post_Code)
        input_post_code.send_keys(text)

    def add_customer(self):
        self.browser.find_element(*AddCustomerLocators.Add_Customer).click()

    def should_be_alert(self):
        alert = self.browser.switch_to.alert
        alert_text = alert.text
        alert.accept()
        assert AddCustomerLocators.Alert_Text in alert_text
