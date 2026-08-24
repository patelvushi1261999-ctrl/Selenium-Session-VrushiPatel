# ============================
# Assignment: Pytest Markers
# ============================

import pytest
import sys

# ----------------------------
# 1. Parametrize test for calculate_discount
# ----------------------------
def calculate_discount(price, coupon):
    if coupon == "SAVE10":
        return price - 10
    elif coupon == "HALFPRICE":
        return price * 0.5
    elif coupon == "SAVE50":
        return price - 50
    return price

@pytest.mark.parametrize(
    "price,coupon,expected",
    [
        (100, "SAVE10", 90),
        (200, "HALFPRICE", 100),
        (300, "SAVE50", 250),
    ]
)
def test_calculate_discount(price, coupon, expected):
    assert calculate_discount(price, coupon) == expected


# ----------------------------
# 2. Smoke vs Regression tests
# ----------------------------
def is_valid_username(username):
    return username.isalnum() and len(username) >= 3

@pytest.mark.smoke
def test_valid_username_smoke():
    assert is_valid_username("User123") is True

@pytest.mark.regression
def test_invalid_username_regression():
    assert is_valid_username("!!") is False

# Run only smoke tests:
# $ pytest -m smoke -v


# ----------------------------
# 3. Skip test if not Android
# ----------------------------
def get_latest_notification():
    return "New message"

@pytest.mark.skip(reason="Only runs on Android platform")
def test_notification_android_only():
    if sys.platform != "android":
        pytest.skip("Skipping because platform is not Android")
    assert get_latest_notification() == "New message"


# ----------------------------
# 4. Expected failure (xfail)
# ----------------------------
def fetch_trending_songs():
    # Simulate API down
    raise ConnectionError("API is down")

@pytest.mark.xfail(reason="Known bug: API down")
def test_fetch_trending_songs():
    fetch_trending_songs()


# ----------------------------
# 5. Parametrize test for format_follower_count
# ----------------------------
def format_follower_count(count):
    if count >= 1_000_000:
        return f"{count/1_000_000:.1f}M"
    elif count >= 1000:
        return f"{count/1000:.1f}K"
    return str(count)

@pytest.mark.parametrize(
    "count,expected",
    [
        (1500, "1.5K"),
        (1200000, "1.2M"),
        (999, "999"),
    ]
)
def test_format_follower_count(count, expected):
    assert format_follower_count(count) == expected

# ---- Example Run Output ----
# $ pytest -v pytest_markers_assignment.py
# collected 7 items
# test_calculate_discount[100-SAVE10-90] PASSED
# test_calculate_discount[200-HALFPRICE-100] PASSED
# test_calculate_discount[300-SAVE50-250] PASSED
# test_valid_username_smoke PASSED
# test_invalid_username_regression PASSED
# test_notification_android_only SKIPPED (Only runs on Android platform)
# test_fetch_trending_songs XFAIL (Known bug: API down)
# test_format_follower_count[1500-1.5K] PASSED
# test_format_follower_count[1200000-1.2M] PASSED
# test_format_follower_count[999-999] PASSED
