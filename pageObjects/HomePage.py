from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pageObjects.BasePage import BasePage


class HomePage(BasePage):
    __field_search_location = (By.CSS_SELECTOR, "#q")
    __button_main_menu = (By.XPATH, "//*[@id='plugin-rhpane-top']/*/*[text()='Menu']")
    __button_windy_logo = (By.CSS_SELECTOR, "#logo")
    __button_login = (
        By.XPATH, "//*[translate(@data-t, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz')='just_login']")
    __div_success_login_msg = (By.ID, "window-message-loggin-ok")
    __list_search_result = (By.CSS_SELECTOR, "#plugin-search a")

    def __init__(self, browser: WebDriver):
        super().__init__(browser)

    def get_field_search_location(self) -> WebElement:
        super()._wait_until_element_clickable(self.__field_search_location)
        return super()._find(self.__field_search_location)

    def enter_search_location(self, location) -> None:
        super()._click(self.__field_search_location)
        super()._type(self.__field_search_location, location)

    def get_button_login(self) -> WebElement:
        super()._wait_until_element_visible(self.__button_login)
        return super()._find(self.__button_login)

    def get_button_main_menu(self) -> WebElement:
        return super()._find(self.__button_main_menu)

    def click_button_login(self):
        super()._click(self.__button_login)

    def click__button_windy_logo(self):
        super()._click(self.__button_windy_logo)

    def get_success_login_msg_banner(self) -> WebElement:
        return self._browser.find_element(*HomePage.__div_success_login_msg)

    def get_search_results(self) -> list[WebElement]:
        super()._wait_until_all_elements_visible(self.__list_search_result)
        return self._browser.find_elements(*HomePage.__list_search_result)
