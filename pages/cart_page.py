from selenium.webdriver.common.by import By
from .base_page import BasePage

class CartPage(BasePage):
    LINE_ITEM = (By.CSS_SELECTOR, ".cart-item, .basket-item")
    CHECKOUT_BTN = (By.CSS_SELECTOR, "div.button[data-location='/checkout/'], a.button[href*='/checkout/'], button.checkout")

    def has_items(self):
        return len(self.driver.find_elements(*self.LINE_ITEM)) > 0

    def click_checkout(self):
        self.click(self.CHECKOUT_BTN)
        return self
