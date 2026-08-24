# ============================
# Assignment: Pytest Fixtures
# ============================

import pytest
from selenium import webdriver

# ----------------------------
# 1. test_instagram_login.py
# ----------------------------
@pytest.fixture
def browser():
    print("\n[Fixture] Starting Chrome browser...")
    driver = webdriver.Chrome()
    yield driver
    print("[Fixture] Closing Chrome browser...")
    driver.quit()

def test_instagram_login(browser):
    browser.get("https://www.instagram.com")
    assert "Instagram" in browser.title


# ----------------------------
# 2. TestSpotifySearch with scope='class'
# ----------------------------
@pytest.fixture(scope="class")
def browser_class():
    print("\n[Fixture] Starting Chrome browser (class scope)...")
    driver = webdriver.Chrome()
    yield driver
    print("[Fixture] Closing Chrome browser (class scope)...")
    driver.quit()

class TestSpotifySearch:
    def test_spotify_homepage_title(self, browser_class):
        browser_class.get("https://www.spotify.com")
        assert "Spotify" in browser_class.title

    def test_spotify_homepage_url(self, browser_class):
        browser_class.get("https://www.spotify.com")
        assert "spotify.com" in browser_class.current_url


# ----------------------------
# 3. conftest.py (shared fixture)
# ----------------------------
# Normally this fixture would live in a separate file named conftest.py
# For demonstration, we include it here.
@pytest.fixture
def shared_browser():
    print("\n[Fixture] Starting shared Chrome browser...")
    driver = webdriver.Chrome()
    yield driver
    print("[Fixture] Closing shared Chrome browser...")
    driver.quit()

def test_flipkart_cart(shared_browser):
    shared_browser.get("https://www.flipkart.com")
    assert "flipkart.com" in shared_browser.current_url


# ----------------------------
# 4. Run pytest with -s flag
# ----------------------------
# Example terminal run:
# $ pytest -s pytest_fixture_assignment.py -v
#
# Output will include the print statements:
# [Fixture] Starting Chrome browser...
# [Fixture] Closing Chrome browser...
# [Fixture] Starting Chrome browser (class scope)...
# [Fixture] Closing Chrome browser (class scope)...
# [Fixture] Starting shared Chrome browser...
# [Fixture] Closing shared Chrome browser...
#
# This shows the setup and teardown order of fixtures.
