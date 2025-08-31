import allure
from selenium import webdriver
from ui_UserAuthorization import UserAuthorization
from ui_search import SearchBook


@allure.title(
        "Тестирование интернет-магазина книг 'Читай-город'"
        )
@allure.description(
    "Тест проверяет корректность работы строки поиска интернет-магазина."
    )
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_search_book_rus_pozitive():
    """
    Тест проверяет работу строки поиска интернет-магазина:
    поиск книги по названию на кириллице.

    :param driver: WebDriver — объект драйвера.
    :param site: str — адресная строка вебсайта интернет-магазина.
    :param author: str — название книги.
    
    """
    driver = webdriver.Firefox()
    with allure.step("Загрузка страницы сайта {site} с авторизацией"):
        book_search_engine = SearchBook(driver)
        book_search_engine.enter("https://www.chitai-gorod.ru/")

    with allure.step("Поиск книги {author} и переход к результатам поиска"):
        book_search_engine.search_field("Ключ из желтого металла")

    with allure.step("Просмотр результатов поиска и возвращение его в переменную"):
        book_search_engine.book_looking()

    assert book_search_engine.book_looking() is not None
    
    driver.quit()

@allure.title(
        "Тестирование интернет-магазина книг 'Читай-город'"
        )
@allure.description(
    "Тест проверяет корректность работы строки поиска интернет-магазина."
    )
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_search_book_eng_pozitive():
    """
    Тест проверяет работу строки поиска интернет-магазина:
    поиск книги по названию на латинице.

    :param driver: WebDriver — объект драйвера.
    :param site: str — адресная строка вебсайта интернет-магазина.
    :param author: str — название книги.
    
    """
    driver = webdriver.Firefox()
    with allure.step("Загрузка страницы сайта {site} с авторизацией"):
        book_search_engine_1 = SearchBook(driver)
        book_search_engine_1.enter("https://www.chitai-gorod.ru/")

    with allure.step("Поиск книги {author} и переход к результатам поиска"):
        book_search_engine_1.search_field("harry potter")

    with allure.step("Просмотр результатов поиска и возвращение его в переменную"):
        book_search_engine_1.book_looking()

    assert book_search_engine_1.book_looking() is not None
    
    driver.quit()

@allure.title(
        "Тестирование интернет-магазина книг 'Читай-город'"
        )
@allure.description(
    "Тест проверяет корректность работы строки поиска интернет-магазина."
    )
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_search_book_numbers_pozitive():
    """
    Тест проверяет работу строки поиска интернет-магазина:
    поиск книги по названию состоящего из цифр.

    :param driver: WebDriver — объект драйвера.
    :param site: str — адресная строка вебсайта интернет-магазина.
    :param author: str — название книги.
    
    """
    driver = webdriver.Firefox()
    with allure.step("Загрузка страницы сайта {site} с авторизацией"):
        book_search_engine_2 = SearchBook(driver)
        book_search_engine_2.enter("https://www.chitai-gorod.ru/")

    with allure.step("Поиск книги {author} и переход к результатам поиска"):
        book_search_engine_2.search_field("1984")

    with allure.step("Просмотр результатов поиска и возвращение его в переменную"):
        book_search_engine_2.book_looking()

    assert book_search_engine_2.book_looking() is not None
    
    driver.quit()

@allure.title(
        "Тестирование интернет-магазина книг 'Читай-город'"
        )
@allure.description(
    "Тест проверяет корректность работы строки поиска интернет-магазина."
    )
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_search_book_autor_book_pozitive():
    """
    Тест проверяет работу строки поиска интернет-магазина:
    поиск книги по названию и автору на кириллице.

    :param driver: WebDriver — объект драйвера.
    :param site: str — адресная строка вебсайта интернет-магазина.
    :param author: str — название книги.
    
    """
    driver = webdriver.Firefox()
    with allure.step("Загрузка страницы сайта {site} с авторизацией"):
        book_search_engine_3 = SearchBook(driver)
        book_search_engine_3.enter("https://www.chitai-gorod.ru/")

    with allure.step("Поиск книги {author} и переход к результатам поиска"):
        book_search_engine_3.search_field("Макс Фрай Лабиринты ехо")

    with allure.step("Просмотр результатов поиска и возвращение его в переменную"):
        book_search_engine_3.book_looking()

    assert book_search_engine_3.book_looking() is not None
    
    driver.quit()

@allure.title(
        "Тестирование интернет-магазина книг 'Читай-город'"
        )
@allure.description(
    "Тест проверяет корректность работы авторизации в интернет-магазине."
    )
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_User_Authorization_pozitive():
    """
    Тест проверяет работу авторизации в интернет-магазине.

    :param driver: WebDriver — объект драйвера.
    :param site: str — адресная строка вебсайта интернет-магазина.
    :param data: str — номер телефона для входа на сайт.
    
    """
    driver = webdriver.Firefox()
    with allure.step("Загрузка страницы сайта {site} с авторизацией"):
        autorization_user_4 = UserAuthorization(driver)
        autorization_user_4.enter("https://www.chitai-gorod.ru/")

    with allure.step("Клик по кнопке входа в личный кабинет"):
        autorization_user_4.autorization()

    with allure.step("Ввод номера телефона {data} и переход на страницус вводом смс-кода"):
        autorization_user_4.data_number("+79493972575")
    
    assert "https://id.tbank.ru" in driver.current_url

    driver.quit()
