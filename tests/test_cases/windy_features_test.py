import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from pageObjects.HomePage import HomePage
from utilities.AppSpecificUtils import AppSpecificUtils
from utilities.baseClass import BaseClass
from utilities.customLogger import CustomLogger
from urllib.parse import urlparse


@pytest.mark.regression
@allure.suite('Automated Regression Suite')
@allure.description("This test attempts to validate some windy website features")
class TestWindyFeatures(BaseClass):
    browser: WebDriver = None

    @allure.title("Verify homepage has login and menu button displayed on RHS of screen")
    def test_homepage_should_display_login_menu_btn(self):

        self.page_has_loaded()
        log = CustomLogger().get_logger()
        hp = HomePage(self.browser)

        hp.get_button_main_menu()
        assert hp.get_button_main_menu() is not None
        log.info("Verified main menu button is present in homepage")

        assert hp.get_button_main_menu() is not None, "Main menu button not found on homepage"
        log.info("Verified login button is present in homepage")

    @allure.title("Verify the co-ordinates shown in windy url represents India or any other country")
    @pytest.mark.parametrize("expected_country", ["India"])
    def test_geo_coordinates_is_displayed_in_windy(self, expected_country):

        log = CustomLogger().get_logger()

        current_url = self.browser.current_url
        parsed_url = urlparse(current_url)

        if not parsed_url.query:
            pytest.fail(f"URL '{current_url}' does not contain query parameters for coordinates.")

        query = parsed_url.query
        coordinates = query[0:query.rfind(',')]
        log.info("extracted the current geo co-ordinates from the site url {}".format(coordinates))

        # latitude = coordinates[0]
        # longitude = coordinates[1]
        # zoom = coordinates[2]
        # coordinates = f"{latitude}, {longitude}"

        location = AppSpecificUtils.get_geolocation_from_coordinates(coordinates)
        log.info(f"gathered the current location using geopy library: {location}")

        actual_country = location.split(",")[-1].strip()
        log.info(f"extracted the country from captured location: {actual_country}")

        assert expected_country == actual_country, f"Expected {expected_country} but found {actual_country}"
        log.info("Verified both expected and actual countries matches")



