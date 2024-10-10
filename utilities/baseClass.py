import pdb
from pathlib import Path
import allure
import pytest
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@pytest.mark.usefixtures('setup')
class BaseClass:

    ROOT_PATH = str(Path(__file__).parent.parent)

    def wait_until_object_visible(self, selector: tuple[str, str], timeout: float = 15) -> bool:

        try:
            wait = WebDriverWait(self.browser, timeout)
            wait.until(ec.visibility_of_element_located(selector))
            return True
        except:
            return False

    def wait_until_object_clickable(self, selector: tuple[str, str], timeout: float = 15) -> bool:

        try:
            wait = WebDriverWait(self.browser, timeout)
            wait.until(ec.element_to_be_clickable(selector))
            return True
        except:
            return False

    def select_text_from_dropdown(self, locator: str, option: str):

        print(self.browser.current_url)
        locator = WebElement(locator)
        selection = Select(locator)
        selection.select_by_visible_text(option)

    def page_has_loaded(self):

        from utilities.customLogger import CustomLogger  # lazy import to avoid circular imports
        log = CustomLogger().get_logger()
        log.info("Checking if {} page has loaded.".format(self.browser.title))
        page_state = self.browser.execute_script('return document.readyState;')
        return page_state == 'complete'

# @allure.title("Logging in application")
# @pytest.fixture(scope='class')
# def login(request, setup, create_categories_json):
#     print('login')
#     # Example: navigate to login page and enter credentials
#     config_data = read_config()
#     email = config_data['email']
#     encoded_password = config_data['password']
#     password = base64.b64decode(encoded_password).decode()
#
#     pdb.set_trace()
#     lp = LoginPage(setup)
#     # lp.get_username().send_keys(username)
#     lp.type_username(email)
#     lp.get_password().send_keys(password)
#     time.sleep(1)
#     lp.get_btn_signin().click()
#
#     # wait for homepage to load
#     hp = HomePage(setup)
#     hp.get_search_product_name()
#
#     return setup
