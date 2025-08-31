import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys 


class UserAuthorization:
    """
    Этот класс представляет:

    - вход на главную страницу сайта
    - авторизацию на сайте по номеру телефона 
    - переход на страницус вводом кода смс
    
    """
    def __init__(self, driver):
        """
        Конструктор класса UserAuthorization

        :param driver: driver — объект драйвера Selenium.
        """
        self._driver = driver

    @allure.step("Загрузка страницы сайта {site} с авторизацией")
    def enter(self,site: str):
        """
        Вводит адрес сайта.

        :param site: Строка адреса сайта.
        :type username: str
        :return: None
        """
        self._driver.get(site)

    @allure.step("Клик по кнопке входа в личный кабинет")
    def autorization(self):
        """
        Кликает кнопку входа в личный кабинет на сайте.
        """
        #Добавляем +20 секунд к задержке и поиск кнопки для прогрузки всех элементов сайта.
        WebDriverWait(self._driver, 20).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'button[class*="search-form__button-search"]')
                ))

        autorize = WebDriverWait(self._driver, 60).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '[aria-label="Меню профиля"]')
                ))
        autorize.click()

    @allure.step("Ввод номера телефона {data} и переход на страницус вводом смс-кода")
    def data_number(self, data: str) -> None:
        """
        Вводит в строку входа номер телефона.
        Кликает RETURN для  перехода на страницу с вводом кода смс.
        Дожидается перехода на страницу с вводом кода смс.

        :param data: Номер телефона.
        :type username: str
        """
        #Добавляем +20 секунд к задержке и поиск кнопки для прогрузки всех элементов сайта.
        WebDriverWait(self._driver, 20).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'button[class*="ui-header-modal__close"]')
                ))

        finder = self._driver.find_element(
            By.CSS_SELECTOR, '[name="phone"]')
        finder.send_keys(data)
        finder.send_keys(Keys.RETURN)

        #Добавляем +20 секунд к задержке для прогрузки всех элементов сайта.
        WebDriverWait(self._driver, 20).until(
            EC.url_contains("https://id.tbank.ru"))
