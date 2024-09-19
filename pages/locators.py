from selenium.webdriver.common.by import By


class MainPageLocators:
    URL = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager"

    Add_Customer = (By.CSS_SELECTOR, "[ng-class='btnClass1']")
    Customers = (By.CSS_SELECTOR, "[ng-class='btnClass3']")


class AddCustomerLocators:
    Alert_Text = "Customer added successfully with customer id :"

    First_Name = (By.CSS_SELECTOR, "[ng-model='fName']")
    Last_Name = (By.CSS_SELECTOR, "[ng-model='lName']")
    Post_Code = (By.CSS_SELECTOR, "[ng-model='postCd']")
    Add_Customer = (By.CLASS_NAME, "btn.btn-default")


class CustomersLocators:
    Table = (By.XPATH, "//table/tbody")
    Rows = (By.TAG_NAME, "tr")
    Cells = (By.TAG_NAME, "td")
    Delete_Customer = (By.CSS_SELECTOR, "[ng-click='deleteCust(cust)']")
    Sort_First_Name = (By.XPATH, "//table/thead//a[contains(text(), 'First Name')]")
