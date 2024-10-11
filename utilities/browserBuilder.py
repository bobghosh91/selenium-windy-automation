import pdb

from selenium import webdriver


class BrowserBuilder:
    def __init__(self, browser_name, headless=False):
        self.browser_name = browser_name
        self.headless = headless
        self.options = None

    def set_options(self):
        if self.browser_name == 'chrome':
            options = webdriver.ChromeOptions()
            options.add_argument('--start-maximized')
            options.add_argument('--disable-popup-blocking')
            options.add_argument('--enable-chrome-browser-cloud-management')
            options.add_argument("disable-features=EdgeExperiencesWithSecurityMessages")
            options.add_argument("disable-infobars")
            options.add_argument("--disable-extensions")
            options.add_argument("--disable-popup-blocking")
            options.add_argument("--disable-notifications")
            options.add_argument("--disable-browser-side-navigation")
            options.set_capability("se:recordVideo", True)
            options.enable_bidi = True

            if self.headless:
                options.add_argument('--headless')
                options.add_argument('--disable-gpu')
                options.add_argument('--window-size=1920x1080')

            self.options = options

        elif self.browser_name == 'edge':
            options = webdriver.EdgeOptions()
            options.use_chromium = True
            options.add_argument('--guest')  # Disable Edge personalized web experience dialog
            options.add_argument('--start-maximized')
            options.add_argument('--enable-chrome-browser-cloud-management')
            options.add_argument("disable-features=EdgeExperiencesWithSecurityMessages")
            options.add_argument("disable-infobars")
            options.add_argument("--disable-extensions")
            options.add_argument("--disable-popup-blocking")
            options.add_argument("--disable-notifications")
            options.add_argument("--disable-browser-side-navigation")
            options.set_capability("se:recordVideo", True)
            options.enable_bidi = True

            if self.headless:
                options.add_argument('--headless')
                options.add_argument('--disable-gpu')
                options.add_argument('--window-size=1920x1080')

            self.options = options

        elif self.browser_name == 'firefox':
            options = webdriver.FirefoxOptions()
            options.add_argument('--start-maximized')
            options.add_argument("disable-infobars")
            options.add_argument("--disable-extensions")
            options.add_argument("--disable-popup-blocking")
            options.add_argument("--disable-notifications")
            options.add_argument("--disable-browser-side-navigation")
            options.set_capability("se:recordVideo", True)
            options.enable_bidi = True

            if self.headless:
                options.add_argument('--headless')
                options.add_argument('--disable-gpu')
                options.add_argument('--window-size=1920x1080')

            self.options = options

    def get_browser(self):
        if self.browser_name == 'chrome':
            # return webdriver.Remote(command_executor='http://192.168.0.104:4444/wd/hub', options=self.options)
            return webdriver.Chrome(options=self.options)
        elif self.browser_name == 'edge':
            # return webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=self.options)
            return webdriver.Edge(options=self.options)
        elif self.browser_name == 'firefox':
            # return webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=self.options)
            return webdriver.Firefox(options=self.options)
        else:
            raise ValueError(f"Unrecognized browser {self.browser_name}")


class BrowserDirector:
    def __init__(self):
        self.builder = None

    def set_builder(self, builder):
        self.builder = builder

    def build_browser(self):
        self.builder.set_options()
        return self.builder.get_browser()
