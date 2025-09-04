from selenium.webdriver.common.by import By
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.waits import wait_visible

PRODUCT_CARD_LINK = (By.CSS_SELECTOR, "a[href*='/product/'], .product-card a, .product a")

def test_add_to_cart_and_open_cart(driver, base_url):
    HomePage(driver, base_url).go("/categorys/3/")
    wait_visible(driver, PRODUCT_CARD_LINK).click()
    ProductPage(driver, base_url).buy()
    HomePage(driver, base_url).open_cart()
    cart = CartPage(driver, base_url)
    assert cart.has_items(), "Expected at least one item in the cart"

def test_checkout_button_visible_or_validation(driver, base_url):
    HomePage(driver, base_url).go("/categorys/3/")
    wait_visible(driver, PRODUCT_CARD_LINK).click()
    ProductPage(driver, base_url).buy()
    HomePage(driver, base_url).open_cart()

    cart = CartPage(driver, base_url)
    cart.click_checkout()

    checkout = CheckoutPage(driver, base_url)
    assert checkout.is_visible(CheckoutPage.PLACEHOLDER_MANDATORY_FIELD) or checkout.has_validation_errors(), \
        "Expected mandatory fields or validation errors on checkout page"
