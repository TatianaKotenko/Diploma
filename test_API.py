import requests
import allure
from api_import import url
from api_import import headers


@allure.title(
        "Тестирование интернет-магазина книг 'Читай-город'"
        )
@allure.description(
    "Тест проверяет корректность работы строки поиска интернет-магазина."
    )
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_author_eng_pozitive():
    """
    Тест проверяет работу строки поиска интернет-магазина:
    поиск книги по названию на латинице.
    """
    with allure.step("Запрос на поиск книги по названию на латинице"):

        response = requests.get(
            url + 'search/product?phrase=harry potter', headers=headers
        )

    with allure.step("Проверка статус-кода"):
        assert response.status_code == 200

@allure.title(
        "Тестирование интернет-магазина книг 'Читай-город'"
        )
@allure.description(
    "Тест проверяет корректность работы строки поиска интернет-магазина."
    )
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_number_pozitive():
    """
    Тест проверяет работу строки поиска интернет-магазина:
    поиск книги по названию состоящего из цифр.
    """
    with allure.step("Запрос на поиск книги по названию с числами"):
        response = requests.get(
            url + 'search/product?phrase=1984', headers=headers
        )

    with allure.step("Проверка статус-кода"):
        assert response.status_code == 200

@allure.title(
        "Тестирование интернет-магазина книг 'Читай-город'"
        )
@allure.description(
    "Тест проверяет корректность работы строки поиска интернет-магазина."
    )
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_author_pozitive():
    """
    Тест проверяет работу строки поиска интернет-магазина:
    поиск книги по названию на кириллице.
    """
    with allure.step("Запрос на поиск книги по названию на кириллице"):
        response = requests.get(
            url + 'search/product?phrase=макс фрай', headers=headers
        )

    with allure.step("Проверка статус-кода"):
        assert response.status_code == 200

@allure.title(
        "Тестирование интернет-магазина книг 'Читай-город'"
        )
@allure.description(
    "Тест проверяет корректность работы строки поиска интернет-магазина."
    )
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_author_negative_PUT_GET():
    """
    Тест проверяет работу строки поиска интернет-магазина:
    поиск книги с некорректным методом PUT вместо GET.
    """
    with allure.step("Запрос на поиск книги с ошибкой в методе: PUT вместо GET"):
        response = requests.put(
            url + 'search/product?phrase=макс фрай', headers=headers
        )

    with allure.step("Проверка статус-кода"):
        assert response.status_code == 405

@allure.title(
        "Тестирование интернет-магазина книг 'Читай-город'"
        )
@allure.description(
    "Тест проверяет корректность работы строки поиска интернет-магазина."
    )
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_author_negative_URL():
    """
    Тест проверяет работу строки поиска интернет-магазина:
    поиск книги с некорректным URL.
    """
    with allure.step("Запрос на поиск книги с некорректным URL(отсутствует 1 буква)"):
        response = requests.get(
            url + 'search/product?phras=макс фрай', headers=headers
        )

    with allure.step("Проверка статус-кода"):
        assert response.status_code == 400
