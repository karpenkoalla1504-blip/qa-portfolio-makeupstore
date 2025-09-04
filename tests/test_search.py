from pages.home_page import HomePage
from pages.search_page import SearchPage

def test_search_existing_brand(driver, base_url):
    HomePage(driver, base_url).open().search("dior")
    sp = SearchPage(driver, base_url)
    assert sp.has_results(), "Expected search results for 'dior'"

def test_search_no_results(driver, base_url):
    HomePage(driver, base_url).open().search("zzzxxyy123")
    sp = SearchPage(driver, base_url)
    assert sp.is_empty() or not sp.has_results(), "Expected empty state for gibberish query"
