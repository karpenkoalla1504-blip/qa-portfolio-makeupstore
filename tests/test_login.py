# tests/test_login.py
import os
import pytest
from pages.login_page import LoginPage

VALID_EMAIL = os.getenv("TEST_LOGIN_EMAIL")
VALID_PASS = os.getenv("TEST_LOGIN_PASSWORD")

@pytest.mark.skipif(
    not (VALID_EMAIL and VALID_PASS),
    reason="Set TEST_LOGIN_EMAIL and TEST_LOGIN_PASSWORD to run positive login test",
)
def test_login_positive(driver, base_url):
    page = LoginPage(driver, base_url).open().login(VALID_EMAIL, VALID_PASS)
    assert page.is_logged_in(), "Expected user to be logged in (logout link visible)"

def test_login_invalid_email_format(driver, base_url):
    page = LoginPage(driver, base_url).open().login("invalid_email", "SomePass123")
    assert page.has_error(), "Expected validation error for invalid email format"

@pytest.mark.skipif(
    not VALID_EMAIL,
    reason="Set TEST_LOGIN_EMAIL to run wrong password test",
)
def test_login_wrong_password(driver, base_url):
    page = LoginPage(driver, base_url).open().login(VALID_EMAIL, "WrongPass!")
    assert page.has_error(), "Expected 'Invalid credentials' error for wrong password"
