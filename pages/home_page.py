from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    SEARCH_ICON = (By.CSS_SELECTOR, "div.search-button[data-popup-handler='search']")
    SEARCH_INPUT = (By.CSS_SELECTOR, "input#search-input[name='q']")
    CART_ICON = (By.CSS_SELECTOR, "div.header-basket")

    def open(self):
        return self.go("/")

    def open_search(self):
        self.click(self.SEARCH_ICON)
        return self

    def search(self, query):
        self.open_search()
        self.type(self.SEARCH_INPUT, query)
        self.driver.switch_to.active_element.send_keys("\n")
        return self

    def open_cart(self):
        self.click(self.CART_ICON)
        return self
