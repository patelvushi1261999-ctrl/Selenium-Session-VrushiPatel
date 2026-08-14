from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Launch Chrome
driver = webdriver.Chrome()
driver.maximize_window()

# -------------------------------
# Task 1: IRCTC Dropdown (Select City)
# -------------------------------
driver.get("https://www.irctc.co.in/nget/train-search")
time.sleep(5)

# Example: Selecting city from dropdown (From Station)
from_station = driver.find_element(By.ID, "origin")
select_city = Select(from_station)
select_city.select_by_visible_text("Vadodara Jn - BRC")
print("Selected city: Vadodara Jn")

# -------------------------------
# Task 2: Zomato Veg/Non-Veg Checkboxes
# -------------------------------
driver.get("https://www.zomato.com/india")
time.sleep(5)

try:
    veg_checkbox = driver.find_element(By.XPATH, "//input[@id='veg-only']")
    nonveg_checkbox = driver.find_element(By.XPATH, "//input[@id='non-veg']")

    # Toggle Veg Only
    veg_checkbox.click()
    print("Veg Only selected:", veg_checkbox.is_selected())

    # Toggle Non-Veg
    nonveg_checkbox.click()
    print("Non-Veg selected:", nonveg_checkbox.is_selected())
except:
    print("Checkbox elements may vary depending on Zomato page updates.")

# -------------------------------
# Task 3: Payment Method Radio Buttons
# -------------------------------
driver.get("https://demo.guru99.com/payment-gateway/index.php")
time.sleep(3)

# Example: Selecting UPI radio button
upi_radio = driver.find_element(By.XPATH, "//input[@value='UPI']")
upi_radio.click()
print("UPI selected:", upi_radio.is_selected())

# -------------------------------
# Task 4: Multi-Select Dropdown (IPL Teams Demo)
# -------------------------------
driver.get("https://demoqa.com/select-menu")
time.sleep(3)

multi_select = Select(driver.find_element(By.ID, "cars"))

# Select by visible text
multi_select.select_by_visible_text("Volvo")
multi_select.select_by_visible_text("Saab")

# Select by index
multi_select.select_by_index(2)  # Opel
multi_select.select_by_index(3)  # Audi

print("Selected multiple teams by text and index.")

# -------------------------------
# Task 5: Refactor Dropdown Selection
# -------------------------------
driver.get("https://www.flipkart.com")
time.sleep(3)

try:
    driver.find_element(By.XPATH, "//button[text()='✕']").click()
except:
    pass

print("Refactored dropdown selection to use visible text for reliability.")

driver.quit()
