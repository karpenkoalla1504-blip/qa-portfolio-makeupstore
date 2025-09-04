from utils.waits import wait_visible, wait_clickable

class BasePage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def go(self, path="/"):
        self.driver.get(self.base_url + path)
        return self

    def click(self, locator):
        wait_clickable(self.driver, locator).click()

    def type(self, locator, text, clear=True):
        el = wait_visible(self.driver, locator)
        if clear:
            el.clear()
        el.send_keys(text)

    def is_visible(self, locator):
        try:
            wait_visible(self.driver, locator, timeout=5)
            return True
        except Exception:
            return False
