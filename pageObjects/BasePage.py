from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    # This is a superclass for page objects. all other classes are subclass to this.

    def __init__(self, browser: WebDriver):
        self._browser = browser

    def _wait_until_element_visible(self, locator: tuple, timeout: float = 15):
        wait = WebDriverWait(self._browser, timeout)
        wait.until(ec.visibility_of_element_located(locator))

    def _wait_until_element_clickable(self, locator: tuple, timeout: float = 15):
        wait = WebDriverWait(self._browser, timeout)
        wait.until(ec.visibility_of_element_located(locator))

    def _wait_until_all_elements_visible(self, locator: tuple, timeout: float = 15):
        wait = WebDriverWait(self._browser, timeout)
        wait.until(ec.presence_of_all_elements_located(locator))

    def _find(self, locator: tuple, timeout: float = 15) -> WebElement:
        self._wait_until_element_visible(locator, timeout)
        return self._browser.find_element(*locator)

    def _type(self, locator: tuple, text: str, timeout: float = 15):
        self._wait_until_element_visible(locator, timeout)
        self._find(locator).send_keys(text)

    def _click(self, locator: tuple, timeout: float = 15):
        self._wait_until_element_visible(locator, timeout)
        self._find(locator).click()
