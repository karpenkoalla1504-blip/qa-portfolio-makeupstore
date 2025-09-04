from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_visible(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))

def wait_clickable(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))

def exists(driver, locator):
    return len(driver.find_elements(*locator)) > 0
