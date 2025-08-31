import allure
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys 


class SearchBook:
    """
    Этот класс представляет:

    - вход на главную страницу сайта
    - поиск книги 
    - просмотров всех найденных книг
    
    """
    def __init__(self, driver):
        """
        Конструктор класса SearchBook

        :param driver: driver — объект драйвера Selenium.
        """
        self._driver = driver

    @allure.step("Загрузка страницы сайта {site} с авторизацией")
    def enter(self, site: str):
        """
        Вводит адрес сайта.

        :param site: Строка адреса сайта.
        :type username: str
        :return: None
        """
        self._driver.get(site)

    @allure.step("Поиск книги {author} и переход к результатам поиска")
    def search_field(self, author: str) -> str:
        """
        Вводит в строку поиска сайта название книги.
        Кликает RETURN для поиска книги.

        :param author: Название книги.
        :type username: str
        """
        # Добавляем +20 секунд к задержке и поиск кнопки для прогрузки всех элементов сайта.
        WebDriverWait(self._driver, 20).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'button[class*="search-form__button-search"]')))

        # Добавляем +20 секунд к задержке для надежности
        finder = WebDriverWait(self._driver, 20).until(
            EC.presence_of_element_located((By.NAME, 'search'))
        )
        finder.send_keys(author)

        finder.send_keys(Keys.RETURN)

    @allure.step("Просмотр результатов поиска и возвращение его в переменную")
    def book_looking(self):
        """
        Отображает результат поиска и возващает его в переменную.

        :param author: Название книги.
        :type username: str
        """
        element = WebDriverWait(self._driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[class="app-catalog__content"]')))
        return element
