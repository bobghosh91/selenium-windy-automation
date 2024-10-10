import pdb
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.CommonPage import CommonPage
from pageObjects.HomePage import HomePage
from utilities.baseClass import BaseClass
from geopy.geocoders import Nominatim

from utilities.customLogger import CustomLogger


class AppSpecificUtils(BaseClass):

    def __init__(self, browser: webdriver.Chrome):
        self.browser = browser
        self.log = CustomLogger().get_logger()

    @staticmethod
    def get_geolocation_from_coordinates(coordinates) -> str:
        geolocator = Nominatim(user_agent="demogeoAPI")
        location = geolocator.reverse(coordinates)
        return location.address

    def change_temperature_scale(self, switch):
        # this method will switch the temperature type to requested scale, cel to far and vice-versa

        match switch:
            case "celsius":
                get_switch_status = self.browser.find_element(By.XPATH,
                                                              "//td[text()='Temperature']/parent::*//a[contains(@data-do,'C')]")
                get_switch_attribute = get_switch_status.get_attribute("class")
                if "selected" in get_switch_attribute:
                    self.log.info("celsius is already selected")
                else:
                    get_switch_status.click()
                    get_switch_attribute = get_switch_status.get_attribute("class")
                    if "selected" in get_switch_attribute:
                        self.log.info("temperature changed to celsius successfully")
                    else:
                        self.log.error("unable to change the temperature switch")

            case "fahrenheit":
                get_switch_status = self.browser.find_element(By.XPATH,
                                                              "//td[text()='Temperature']/parent::*//a[contains(@data-do,'F')]")
                get_switch_attribute = get_switch_status.get_attribute("class")
                if "selected" in get_switch_attribute:
                    self.log.info("fahrenheit is already selected")
                else:
                    get_switch_status.click()
                    get_switch_attribute = get_switch_status.get_attribute("class")
                    if "selected" in get_switch_attribute:
                        self.log.info("temperature changed to fahrenheit successfully")
                    else:
                        self.log.error("unable to change the temperature switch")


class PageNavigation(BaseClass):

    def __init__(self, browser):
        self.browser = browser

    def navigate_to_homepage(self):
        hp = HomePage(self.browser)
        hp.click__button_windy_logo()
        time.sleep(3)

    def navigate_to_settings(self):
        hp = HomePage(self.browser)
        cp = CommonPage(self.browser)

        hp.get_button_main_menu().click()
        cp.click_button_settings()
