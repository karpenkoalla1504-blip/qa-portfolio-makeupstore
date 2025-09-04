from selenium.webdriver.common.by import By
from .base_page import BasePage

class CheckoutPage(BasePage):
    PLACEHOLDER_MANDATORY_FIELD = (By.CSS_SELECTOR, "input[required], select[required]")
    CONFIRM_ORDER = (By.XPATH, "//button[contains(., 'Place order') or contains(., 'Pay') or contains(., 'Confirm')]")
    ERROR = (By.XPATH, "//*[contains(@class,'error') or contains(.,'required')]")
    ORDER_CONF = (By.XPATH, "//*[contains(., 'Order') and contains(., 'confirmation')]")

    def has_validation_errors(self):
        return len(self.driver.find_elements(*self.ERROR)) > 0

    def is_on_confirmation(self):
        return self.is_visible(self.ORDER_CONF)
