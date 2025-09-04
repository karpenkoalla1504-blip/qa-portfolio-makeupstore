from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    EMAIL = (By.NAME, "email")
    PASSWORD = (By.NAME, "password")
    SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")
    LOGOUT_LINK = (By.XPATH, "//a[contains(., 'Logout') or contains(., 'Sign out')]")
    ERROR = (By.XPATH, "//*[contains(@class,'error') or contains(text(),'Invalid')]")

    def open(self):
        return self.go("/login/")

    def login(self, email, password):
        self.type(self.EMAIL, email)
        self.type(self.PASSWORD, password)
        self.click(self.SUBMIT)
        return self

    def is_logged_in(self):
        return self.is_visible(self.LOGOUT_LINK)

    def has_error(self):
        return self.is_visible(self.ERROR)
