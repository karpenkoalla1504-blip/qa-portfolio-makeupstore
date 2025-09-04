from selenium.webdriver.common.by import By
from .base_page import BasePage

class SearchPage(BasePage):
    PRODUCT_CARD = (By.CSS_SELECTOR, ".product-card, .product")
    EMPTY_STATE = (By.XPATH, "//*[contains(., 'No results') or contains(., 'ничего не найдено')]")

    def has_results(self):
        return len(self.driver.find_elements(*self.PRODUCT_CARD)) > 0

    def is_empty(self):
        return len(self.driver.find_elements(*self.EMPTY_STATE)) > 0
