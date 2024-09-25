import allure

from data.data import Config
from pages.customers_page import CustomersPage
from pages.main_page import MainPage


@allure.feature("Customers page")
@allure.story("UI")
@allure.title("Сортировка клиентов по имени")
@allure.description(
    """
    Предусловия:
        1. Открыть браузер
        2. Перейти на страницу: https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager
    
    Шаги:
        1. Нажать кнопку Customers
        2. Получить список имен First Name из таблицы Customers
        3. Нажать на заголовок колонки First Name для сортировки
        4. Получить отсортированный список имен First Name из таблицы Customers
    
    Ожидаемый результат:
        Отсортированный список совпадает с изначальным списком, отсортированным в Python по убыванию
    """
)
def test_sort_customers_by_first_name(browser):
    with allure.step("Открытие главной страницы"):
        main_page = MainPage(browser, Config.URL)
        main_page.open_page()

    with allure.step("Нажатие кнопки Customers"):
        main_page.go_to_customers_page()
        customers_page = CustomersPage(browser, browser.current_url)

    with allure.step("Получение списка имен First Name из таблицы Customers"):
        first_names = customers_page.get_list_of_first_name()

    with allure.step("Нажатие на заголовок колонки First Name для сортировки"):
        customers_page.sort_first_name()

    with allure.step("Получение отсортированного списка имен First Name из таблицы Customers"):
        first_names_sorted = customers_page.get_list_of_first_name()

    with allure.step(
            "Проверка того, что отсортированный список совпадает с изначальным списком, отсортированным в Python по убыванию"):
        customers_page.should_be_sorted(first_names, first_names_sorted)


@allure.feature("Customers page")
@allure.story("UI")
@allure.title("Удаление клиента")
@allure.description(
    """
    Предусловия:
        1. Открыть браузер
        2. Перейти на страницу: https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager
    
    Шаги:
        1. Нажать кнопку Customers
        2. Извлечь из таблицы Customers список имен First Name
        3. Вычислить длину каждого имени
        4. Вычислить среднее арифметическое длин имен
        5. Найти имя, длина которого наиболее близка к среднему арифметическому
        6. Найти строку в таблице Customers, соответствующую найденному имени
        7. Нажать кнопку Delete в соответствующей строке

    Ожидаемый результат:
        Общее количество строк в таблице Customers сократилась на 1
    """
)
def test_delete_customer(browser):
    with allure.step("Открытие главной страницы"):
        main_page = MainPage(browser, Config.URL)
        main_page.open_page()

    with allure.step("Нажатие кнопки Customers"):
        main_page.go_to_customers_page()
        customers_page = CustomersPage(browser, browser.current_url)

    with allure.step("Извлечение из таблицы Customers списка имен First Name"):
        first_names = customers_page.get_list_of_first_name()

    with allure.step("Вычисление длины каждого имени"):
        length_of_first_names = customers_page.get_lengths(first_names)

    with allure.step("Вычисление среднего арифметического длин имен"):
        average_length = customers_page.get_average_length(length_of_first_names)

    with allure.step("Нахождение имени, длина которого наиболее близка к среднему арифметическому"):
        first_name_to_delete = customers_page.get_first_name_to_delete(first_names, average_length)

    with allure.step("Нахождение строки в таблице Customers, соответствующей найденному имени"):
        index_to_delete = customers_page.get_first_name_index_to_delete(first_names, first_name_to_delete)

    with allure.step("Нажатие кнопки Delete в соответствующей строке"):
        customers_page.delete_customer(index_to_delete)

    with allure.step("Проверка того, что общее количество строк в таблице Customers сократилась на 1"):
        customers_page.should_be_delete(len(first_names))
