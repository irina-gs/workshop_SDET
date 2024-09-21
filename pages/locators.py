from selenium.webdriver.common.by import By


class MainPageLocators:
    ADD_CUSTOMER = (By.CSS_SELECTOR, "[ng-class='btnClass1']")
    CUSTOMERS = (By.CSS_SELECTOR, "[ng-class='btnClass3']")


class AddCustomerLocators:
    FIRST_NAME = (By.CSS_SELECTOR, "[ng-model='fName']")
    LAST_NAME = (By.CSS_SELECTOR, "[ng-model='lName']")
    POST_CODE = (By.CSS_SELECTOR, "[ng-model='postCd']")
    ADD_CUSTOMER = (By.CLASS_NAME, "btn.btn-default")


class CustomersLocators:
    TABLE = (By.XPATH, "//table/tbody")
    ROWS = (By.TAG_NAME, "tr")
    CELLS = (By.TAG_NAME, "td")
    DELETE_CUSTOMER = (By.CSS_SELECTOR, "[ng-click='deleteCust(cust)']")
    SORT_FIRST_NAME = (By.XPATH, "//table/thead//a[contains(text(), 'First Name')]")
