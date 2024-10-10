# retryable Selenium options
import time

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# retry a test step a maximum of 3 times within 30 seconds:
def find_element(by, value, max_retries=3, timeout=30):
    start_time = time.time()
    for i in range(max_retries):
        try:
            element = driver.find_element(by, value)
            return element
        except WebDriverException as e:
            if (i == max_retries - 1) and (time.time() - start_time > timeout):
                raise e
            time.sleep(10)  # sleep for 10 seconds
            continue


# example usage
driver = webdriver.Chrome()

try:
    element = find_element(By.ID, "someid")
    element.click()
except Exception as e:
    print("Element not found")

driver.quit()
