from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch Chrome
driver = webdriver.Chrome()
driver.maximize_window()

# -------------------------------
# Task 1: Flipkart New Tab Handling
# -------------------------------
driver.get("https://www.flipkart.com")
time.sleep(3)

# Close login popup if it appears
try:
    driver.find_element(By.XPATH, "//button[text()='✕']").click()
except:
    pass

# Click 'Become a Seller' link (opens new tab)
seller_link = driver.find_element(By.LINK_TEXT, "Become a Seller")
seller_link.click()

# Get window handles
handles = driver.window_handles
main_window = driver.current_window_handle

# Switch to new tab
driver.switch_to.window(handles[1])
print("New Tab Title:", driver.title)

# Switch back to original tab
driver.switch_to.window(main_window)
print("Original Tab Title:", driver.title)

# -------------------------------
# Task 2: Zomato Navigation Flow
# -------------------------------
driver.get("https://www.zomato.com/india")
time.sleep(3)

# Click a city link (example: Ahmedabad)
city_link = driver.find_element(By.LINK_TEXT, "Ahmedabad")
city_link.click()
time.sleep(2)

# Navigate back
driver.back()
print("Navigated Back:", driver.title)
time.sleep(2)

# Navigate forward
driver.forward()
print("Navigated Forward:", driver.title)
time.sleep(2)

# Refresh page
driver.refresh()
print("Page Refreshed:", driver.title)

# -------------------------------
# Task 3: Paytm Offer Window
# -------------------------------
driver.get("https://paytm.com")
time.sleep(3)

# Example: Click an offer banner (replace with actual locator)
try:
    offer_banner = driver.find_element(By.XPATH, "//a[contains(@href,'offers')]")
    offer_banner.click()

    # Switch to new window
    handles = driver.window_handles
    driver.switch_to.window(handles[1])
    offer_headline = driver.find_element(By.TAG_NAME, "h1").text
    print("Offer Headline:", offer_headline)

    # Switch back to main window
    driver.switch_to.window(handles[0])
    print("Main Page Title:", driver.title)
except:
    print("Offer banner locator may vary.")

# -------------------------------
# Task 4: Myntra Multiple Tabs Handling
# -------------------------------
driver.get("https://www.myntra.com")
time.sleep(3)

# Example: Open multiple product links in new tabs
products = driver.find_elements(By.XPATH, "//a[contains(@href,'/men-tshirts')]")[:3]
main_window = driver.current_window_handle

for product in products:
    product.send_keys(webdriver.common.keys.Keys.CONTROL + webdriver.common.keys.Keys.RETURN)
    time.sleep(1)

# Loop through all tabs
for handle in driver.window_handles:
    driver.switch_to.window(handle)
    print("Tab URL:", driver.current_url)
    if handle != main_window:
        driver.close()

# Switch back to main window
driver.switch_to.window(main_window)
print("Back to Main Window:", driver.title)

# Close browser
driver.quit()
