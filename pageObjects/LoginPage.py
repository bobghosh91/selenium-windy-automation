from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pageObjects.BasePage import BasePage


class LoginPage(BasePage):
    __field_email = (By.ID, "email")
    __field_password = (By.ID, "password")
    __btn_loginpage_login = (By.ID, "submitLogin")

    def __init__(self, browser: WebDriver):
        super().__init__(browser)

    def get_field_email(self) -> WebElement:
        return super()._find(self.__field_email)

    def get_password(self) -> WebElement:
        # making get password return a web element(-> webElement)
        return self._browser.find_element(*LoginPage.__field_password)

    def get_loginpage_login_btn(self) -> WebElement:
        return self._browser.find_element(*LoginPage.__btn_loginpage_login)

    def type_email_address(self, emailtext):
        super()._type(self.__field_email, emailtext)

    def type_password(self, password):
        super()._type(self.__field_password, password)

    def click_loginpage_login_btn(self):
        super()._click(self.__btn_loginpage_login)