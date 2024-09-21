from pages.base_page import BasePage
from pages.locators import CustomersLocators


class CustomersPage(BasePage):
    @staticmethod
    def get_lengths(first_names):
        return [len(first_name) for first_name in first_names]

    @staticmethod
    def get_average_length(lengths):
        return sum(lengths) / len(lengths)

    @staticmethod
    def get_first_name_to_delete(first_names, average_length):
        return min(first_names, key=lambda first_name: abs(len(first_name) - average_length))

    @staticmethod
    def get_first_name_index_to_delete(first_names, first_name_to_delete):
        return first_names.index(first_name_to_delete)

    @staticmethod
    def should_be_sorted(first_names, first_names_sorted):
        assert first_names_sorted == sorted(first_names, reverse=True)

    def get_list_of_first_name(self):
        rows = self.browser.find_element(*CustomersLocators.TABLE).find_elements(*CustomersLocators.ROWS)

        column_index = 0
        first_names = []

        for row in rows:
            cells = row.find_elements(*CustomersLocators.CELLS)
            first_names.append(cells[column_index].text)

        return first_names

    def delete_customer(self, index_to_delete):
        row = self.browser.find_element(*CustomersLocators.TABLE).find_elements(*CustomersLocators.ROWS)[
            index_to_delete]
        row.find_element(*CustomersLocators.DELETE_CUSTOMER).click()

    def should_be_delete(self, length_before_deleting):
        rows = self.browser.find_element(*CustomersLocators.TABLE).find_elements(*CustomersLocators.ROWS)
        length_after_deleting = len(rows)

        assert length_after_deleting == length_before_deleting - 1

    def sort_first_name(self):
        self.browser.find_element(*CustomersLocators.SORT_FIRST_NAME).click()
