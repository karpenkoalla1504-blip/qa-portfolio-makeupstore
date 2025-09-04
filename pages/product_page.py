from selenium.webdriver.common.by import By
from .base_page import BasePage

class ProductPage(BasePage):
    TITLE = (By.CSS_SELECTOR, "h1, .product-title")
    PRICE = (By.CSS_SELECTOR, ".price, [data-price]")
    BUY_BUTTON = (By.XPATH, "//*[self::button or self::div][contains(., 'Buy') or contains(@class,'buy') or @data-action='buy']")

    def buy(self):
        self.click(self.BUY_BUTTON)
        return self
