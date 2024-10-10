from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from pageObjects.BasePage import BasePage


class CommonPage(BasePage):

    __button_settings = (By.XPATH, '//*[contains(@class,"menu-top__column-wrapper")]//a[text()="Settings"]')

    def __init__(self, browser:WebDriver):
        super().__init__(browser)

    def click_button_settings(self):
        self._wait_until_element_clickable(self.__button_settings)
        super()._click(self.__button_settings)
        # return self._browser.find_element(*CommonPage.__button_settings)