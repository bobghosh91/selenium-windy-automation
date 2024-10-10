import base64
import json
import os.path
import pdb
import time
import warnings
import allure
import pytest
from selenium import webdriver
from configs.configurations import read_config
from utilities.browserBuilder import BrowserBuilder, BrowserDirector


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="please choose browser type",
        choices=("chrome", "edge", "firefox", "safari")
    )
    parser.addoption(
        "--headless", action="store_true", help="Run tests in headless mode",
    )


# change scope to 'function' launch browser for each function
@pytest.fixture(scope='class')
def browser_name(request):
    name = request.config.getoption('--browser_name')
    with allure.step(f"Selected browser: {name}"):
        return name


@pytest.fixture(scope='class')
def headless(request):
    hmode = request.config.getoption('--headless')
    with allure.step(f"Selected headless mode: {hmode}"):
        return hmode


@pytest.fixture(scope='class')
def create_categories_json():
    output = [
        {
            "name": "Skipped tests",
            "messageRegex": ".*",
            "matchedStatuses": ["skipped"]
        },
        {
            "name": "Element not found",
            "traceRegex": ".*NoSuchElementError.*",
            "matchedStatuses": ["failed"]
        },
        {
            "name": "Broken tests",
            "traceRegex": "Error.*",
            "matchedStatuses": ["failed"]
        },
        {
            "name": "Test defect",
            "messageRegex": ".*Expected is not a String or a RegExp.*",
            "matchedStatuses": ["failed"]
        },
        {
            "name": "Product defect",
            "traceRegex": ".*Failed expectation.*",
            "matchedStatuses": ["failed"]
        },
        {
            "name": "Passed tests",
            "matchedStatuses": ["passed"]
        }
    ]

    try:
        file_path = os.path.join(os.getcwd(), r'reports/allure-results', 'categories.json')
        with open(file_path, 'w') as json_file:
            json.dump(output, json_file, indent=1)
        print('categories.json file successfully created')
    except (Exception, PermissionError) as e:
        warnings.warn(f'error writing json object to categories.json: {e}')


@allure.title("Setting up for the test")
@pytest.fixture(scope='class', autouse=True)
def setup(request, browser_name, headless):
    # print('setup')
    config_data = read_config()
    base_url = config_data['url']

    # Create builder and director
    builder = BrowserBuilder(browser_name, headless)
    director = BrowserDirector()
    director.set_builder(builder)

    # Build the browser
    browser = director.build_browser()

    # Set implicit wait
    browser.implicitly_wait(15)

    # Attach the browser instance to the class
    request.cls.browser = browser
    browser.get(base_url)

    yield browser

    # Tear down: Quit the driver
    @allure.step("Quitting the browser")
    def teardown():
        browser.quit()

    teardown()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # This hook is used to capture test result information
    outcome = yield
    rep = outcome.get_result()

    if (rep.when == 'call' or rep.when == 'setup') and (rep.failed or rep.skipped):
        # Only take a screenshot if the test failed during the call phase
        browser = item.funcargs['setup']
        allure.attach(browser.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)


def pytest_configure(config):
    # Ensure the 'screenshots' directory exists
    if not os.path.exists('screenshots'):
        pass
