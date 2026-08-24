# ============================
# Assignment: Pytest Practice
# ============================

# 1. test_sample.py
def test_addition():
    assert 2 + 3 == 5


# 2. test_zomato_cart.py
# Assume apply_discount is defined in zomato_cart.py
def apply_discount(amount, discount):
    return amount - discount

def test_discount_applied():
    assert apply_discount(100, 10) == 90


# 3. Renamed check_login.py → test_login.py
# Original functions were check_username, check_password
def test_username():
    return True

def test_password():
    return True

# Observation: pytest only discovers functions starting with 'test_' inside files named 'test_*.py'


# 4. test_followers.py
def format_count(n):
    if n >= 1000:
        return f"{n/1000:.1f}K"
    return str(n)

def test_follower_count():
    assert format_count(1500) == '1.5K'


# 5. test_email.py
def is_valid_email(email: str) -> bool:
    return "@" in email and "." in email

def test_valid_email():
    assert is_valid_email("user@example.com") is True

def test_invalid_email():
    assert is_valid_email("userexample.com") is False

# ---- Test Output ----
# $ pytest pytest_assignment.py -v
# ============================= test session starts =============================
# collected 7 items
# pytest_assignment.py::test_addition PASSED                              [ 14%]
# pytest_assignment.py::test_discount_applied PASSED                      [ 28%]
# pytest_assignment.py::test_username PASSED                              [ 42%]
# pytest_assignment.py::test_password PASSED                              [ 57%]
# pytest_assignment.py::test_follower_count PASSED                        [ 71%]
# pytest_assignment.py::test_valid_email PASSED                           [ 85%]
# pytest_assignment.py::test_invalid_email PASSED                         [100%]
# ============================== 7 passed in 0.03s ==============================
