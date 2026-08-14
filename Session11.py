from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Launch Chrome
driver = webdriver.Chrome()
driver.maximize_window()

# -------------------------------
# Task 1: Myntra Alert
# -------------------------------
driver.get("https://www.myntra.com")
time.sleep(3)

# Trigger JavaScript alert
driver.execute_script('alert("Welcome to Myntra Offers!")')

# Switch to alert and accept
alert = driver.switch_to.alert
print("Alert text:", alert.text)
alert.accept()
print("Alert accepted")

# -------------------------------
# Task 2: Confirm Dialog (Herokuapp)
# -------------------------------
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
time.sleep(2)

# Click JS Confirm button
driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()

# Switch to alert and dismiss
confirm_alert = driver.switch_to.alert
print("Confirm text:", confirm_alert.text)
confirm_alert.dismiss()
print("Confirm dismissed")

# -------------------------------
# Task 3: W3Schools Iframe
# -------------------------------
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe")
time.sleep(3)

# Switch into first iframe
driver.switch_to.frame("iframeResult")

# Inside iframe, print title
iframe_title = driver.title
print("Iframe page title:", iframe_title)

# Switch back to main content
driver.switch_to.default_content()
print("Switched back to main content")

# -------------------------------
# Task 4: Zomato Review Prompt (Custom HTML Demo)
# -------------------------------


driver.get("file:///C:/Users/YourName/review_demo.html")  # replace with your local path
time.sleep(2)

# Switch into iframe
driver.switch_to.frame("reviewFrame")

# Trigger prompt alert via JavaScript
driver.execute_script('alert(prompt("Enter your review:"))')

# Switch to alert, enter review, and accept
prompt_alert = driver.switch_to.alert
prompt_alert.send_keys("Great food and service!")
prompt_alert.accept()
print("Review submitted via prompt alert")

driver.quit()
