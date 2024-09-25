import allure

from data.data import Config
from pages.add_customer_page import AddCustomerPage
from pages.main_page import MainPage


@allure.feature("Add customer page")
@allure.story("UI")
@allure.title("Создание клиента")
@allure.description(
    """
    Предусловия:
        1. Открыть браузер
        2. Перейти на страницу: https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager
    
    Шаги:
        1. Нажать кнопку Add Customer
        2. Сгенерировать для поля Post Code номер из 10 цифр
        3. Сгенерировать для поля First Name имя на основе Post Code согласно следующей логике:
            - Post Code условно разбить на двузначные цифры (получится 5 цифр)
            - Каждую цифру преобразовать в букву английского алфавита по порядку от 0 до 25. Если цифра больше 25, то начинать с 26 как с 0. Т.е. 0 - a, 26 - тоже a, 52 – тоже a, и т.д.
            Пример: 0001252667 = abzap 
        4. Заполнить поле First Name сгенерированным именем
        5. Заполнить поле Last Name произвольной строкой
        6. Заполнить поле Post Code сгенерированным номером
        7. Нажать кнопку Add Customer
    
    Ожидаемый результат:
        Появилось всплывающее окно с сообщением Customer added successfully with customer id :
    """
)
def test_add_customer(browser, last_name):
    with allure.step("Открытие главной страницы"):
        main_page = MainPage(browser, Config.URL)
        main_page.open_page()

    with allure.step("Нажатие кнопки Add Customer"):
        main_page.go_to_add_customer_page()
        add_customer_page = AddCustomerPage(browser, browser.current_url)

    with allure.step("Генерация номера для поля Post Code"):
        post_code = add_customer_page.generate_post_code()

    with allure.step("Генерация имени для поля First Name"):
        first_name = add_customer_page.generate_first_name(post_code)

    with allure.step("Заполнение поля First Name сгенерированным именем"):
        add_customer_page.fill_in_first_name_field(first_name)

    with allure.step("Заполнение поля Last Name произвольной строкой"):
        add_customer_page.fill_in_last_name_field(last_name)

    with allure.step("Заполнение поля Post Code сгенерированным номером"):
        add_customer_page.fill_in_post_code_field(post_code)

    with allure.step("Нажатие кнопки Add Customer"):
        add_customer_page.add_customer()

    with allure.step(
            "Проверка появления всплывающего окна с сообщением Customer added successfully with customer id :"):
        add_customer_page.should_be_alert()
