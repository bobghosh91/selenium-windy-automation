import base64
import pdb
import time
import allure
import pytest
from selenium.webdriver.common.by import By
from configs.configurations import read_config
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities.AppSpecificUtils import AppSpecificUtils, PageNavigation
from utilities.XLUtils import XLUtils
from utilities.baseClass import BaseClass
from utilities.customLogger import CustomLogger
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.mark.sanity
@allure.suite('Automated Regression Suite')
@allure.description("This test attempts to validate some windy website features")
class TestWindyFeatures(BaseClass):
    browser: WebDriver = None

    @allure.title("Verify successful login of a valid user on the windy website")
    def test_login_functionality_valid_user(self):
        self.page_has_loaded()
        log = CustomLogger().get_logger()
        hp = HomePage(self.browser)
        lp = LoginPage(self.browser)

        hp.click_button_login()
        lp.get_field_email()
        log.info("Verified email address field appears on screen")

        config_data = read_config()
        email = config_data['email']
        encoded_password = config_data['password']
        password = base64.b64decode(encoded_password).decode()

        lp.type_email_address(email)
        log.info(f"Entered {email} into the 'email address' field")
        lp.type_password(password)
        log.info(f"Entered password into the 'password' field")

        lp.click_loginpage_login_btn()
        log.info('Clicked on the login button')

        if not self.wait_until_object_visible((By.ID, "window-message-loggin-ok")):
            log.error('user login unsuccessful')
            pytest.fail("user was not able to login successfully")

        successtext = hp.get_success_login_msg_banner().text
        assert "successfully" in successtext
        log.info('user login successful')

    @pytest.mark.parametrize("test_case_id", ["TC_01"])
    @allure.title("Verify user able to search location and report temperature")
    def test_search_city_gather_temperature(self, test_case_id):
        log = CustomLogger().get_logger()
        hp = HomePage(self.browser)
        asu = AppSpecificUtils(self.browser)
        pagenav = PageNavigation(self.browser)
        test_data = XLUtils.getTestData(test_case_id)

        pagenav.navigate_to_settings()
        log.info("navigated to settings page")
        asu.change_temperature_scale(test_data["Temperature Scale"])

        hp.get_field_search_location()
        hp.enter_search_location(test_data['Location'])
        log.info("Entered 'Pune city' in the search location")

        places = hp.get_search_results()
        for place in places:
            if place.text.strip() == test_data['Location']:
                place.click()
                log.info("clicked on pune city option from the list")

        self.wait_until_object_visible((By.XPATH, "//tr[contains(@class,'td-temp')]/td[1]"))
        pune_temperature = self.browser.find_element(By.XPATH, "//tr[contains(@class,'td-temp')]/td[1]")
        log.info("waited for temperature to be displayed on screen")

        # Validate the element is present
        assert pune_temperature.is_displayed(), log.info("Pune temperature is not displayed on the page")
        log.info("validated that temperature is displayed on screen")

        # Validate the temperature displayed is between range 18 to 35
        temp_int = int(pune_temperature.text.replace("°", ""))
        assert int(test_data['Minimum Temperature']) <= temp_int <= int(test_data['Maximum Temperature']), \
            "Current Pune temperature is not moderate today"

        self.browser.find_element(By.CSS_SELECTOR, '[data-plugin="bottom-pane"] [class="closing-x"]').click()
        log.info("closed the temperature bottom pane")

    @pytest.mark.parametrize("test_case_id", ["TC_02"])
    @allure.title("Verify user able to change temperature from celsius to fahrenheit")
    def test_change_temperature_c_to_f(self, test_case_id):

        test_data = XLUtils.getTestData(test_case_id)
        asu = AppSpecificUtils(self.browser)
        pagenav = PageNavigation(self.browser)
        log = CustomLogger().get_logger()

        pagenav.navigate_to_homepage()
        pagenav.navigate_to_settings()
        log.info("navigated to settings page")

        asu.change_temperature_scale(test_data["Temperature Scale"])
        log.info("changed the temperature setting")

        get_mumbai_city = self.browser.find_element(By.XPATH, f'//*[@data-label="{test_data["Location"]}"]')
        get_mumbai_city_temp = int(get_mumbai_city.get_attribute("data-temp").replace("°", ""))

        # Validate the element is present
        assert get_mumbai_city.is_displayed(), log.info("mumbai temperature is not displayed on the page")

        # Validate the temperature displayed is between range 65 to 95
        log.info(get_mumbai_city_temp)
        assert int(test_data['Minimum Temperature']) <= get_mumbai_city_temp <= int(test_data['Maximum Temperature']), \
            "Current Mumbai temperature is not moderate today"

    @allure.title("Verify the menu and other options are displayed to the right pane")
    def test_menu_settings_displayed_on_rhs(self):

        pagenav = PageNavigation(self.browser)
        log = CustomLogger().get_logger()

        pagenav.navigate_to_homepage()

        current_place = self.browser.find_element(By.CSS_SELECTOR, "#q").get_property("value")
        log.info(f"the current location on map is: {current_place}")

        self.wait_until_object_clickable((By.CSS_SELECTOR, "#plugin-rhpane-top"))

        # main_div = self.browser.find_element(By.XPATH, '//*[@id="plugin-rhpane-top"]')
        # target_div = self.browser.find_element(locate_with(By.TAG_NAME, "span").above(main_div))

        parent_element = self.browser.find_element(By.XPATH, '//*[@id="plugin-rhpane-top"]/parent::*')
        pane_value = parent_element.get_attribute("data-plugin")
        assert "rh" in pane_value
        log.info("verified the panes and options are in RHS")
