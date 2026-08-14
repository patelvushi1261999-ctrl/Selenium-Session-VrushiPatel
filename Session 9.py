from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# Launch Chrome
driver = webdriver.Chrome()
driver.maximize_window()

# -------------------------------
# Task 1: Myntra Logo with Implicit Wait
# -------------------------------
driver.implicitly_wait(10)  # implicit wait for all elements
driver.get("https://www.myntra.com")

# Wait until logo is visible (implicit wait handles this)
logo = driver.find_element(By.XPATH, "//a[@class='myntra-logo']")
print("Myntra logo visible:", logo.is_displayed())

# Click on 'Men' menu
men_menu = driver.find_element(By.XPATH, "//a[text()='Men']")
men_menu.click()
print("Clicked on Men menu")

# -------------------------------
# Task 2: Zomato Login with Explicit Wait
# -------------------------------
driver.get("https://www.zomato.com/india")
time.sleep(3)

# Example: Click login button
try:
    login_button = driver.find_element(By.XPATH, "//a[text()='Log in']")
    login_button.click()

    # Enter phone number (dummy example)
    phone_input = driver.find_element(By.NAME, "phone")
    phone_input.send_keys("9999999999")

    # Explicit wait for OTP field
    wait = WebDriverWait(driver, 15)
    otp_field = wait.until(EC.visibility_of_element_located((By.NAME, "otp")))
    print("OTP field visible:", otp_field.is_displayed())
except:
    print("Login flow may vary depending on Zomato updates.")

# -------------------------------
# Task 3: BookMyShow Movies with Fluent Wait
# -------------------------------
driver.get("https://in.bookmyshow.com")
time.sleep(3)

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def movies_loaded(driver):
    elements = driver.find_elements(By.XPATH, "//div[contains(@class,'movie-card')]//h4")
    return elements if len(elements) >= 3 else False

try:
    fluent_wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[TimeoutException])
    movies = fluent_wait.until(movies_loaded)
    print("First 3 movies:")
    for movie in movies[:3]:
        print("-", movie.text)
except TimeoutException:
    print("Movies did not load in time.")

# -------------------------------
# Task 4: Flipkart Add to Cart with Explicit Wait
# -------------------------------
driver.get("https://www.flipkart.com")
time.sleep(2)

# Close login popup
try:
    driver.find_element(By.XPATH, "//button[text()='✕']").click()
except:
    pass

# Example: Explicit wait for Add to Cart button
try:
    wait = WebDriverWait(driver, 15)
    add_to_cart = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Add to Cart']")))
    add_to_cart.click()
    print("Clicked Add to Cart button")
except TimeoutException:
    print("Add to Cart button not clickable in time.")

# -------------------------------
# Task 5: IRCTC Train Search Wait Strategy
# -------------------------------
driver.get("https://www.irctc.co.in/nget/train-search")

driver.implicitly_wait(10)  # general elements

try:
    wait = WebDriverWait(driver, 20)
    results = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class,'train_avl_enq_box')]")))
    print("Train results loaded successfully")
except TimeoutException:
    print("Train results did not load in time")
driver.quit()
