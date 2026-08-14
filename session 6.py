from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

# Task 1: Flipkart Search Bar
driver.get("https://www.flipkart.com")
time.sleep(2)
try:
    driver.find_element(By.XPATH, "//button[text()='✕']").click()
except:
    pass
search_css = driver.find_element(By.CSS_SELECTOR, "input[title='Search for products, brands and more']")
print("Flipkart Search Bar (CSS):", search_css.get_attribute("outerHTML"))
search_xpath = driver.find_element(By.XPATH, "//input[@title='Search for products, brands and more']")
print("Flipkart Search Bar (XPath):", search_xpath.get_attribute("outerHTML"))

#-------------------------------------------------------------
# Task 2: Zomato Restaurant Name
#-------------------------------------------------------------

driver.get("https://www.zomato.com/india")
time.sleep(3)
zomato_css = driver.find_element(By.CSS_SELECTOR, "a[class*='sc-']")
print("Zomato Restaurant Name (CSS):", zomato_css.text)
zomato_xpath = driver.find_element(By.XPATH, "(//a[contains(@class,'sc-') and text()])[1]")
print("Zomato Restaurant Name (XPath):", zomato_xpath.text)

#-------------------------------------------------------------
# Task 3: Myntra Login/Sign In Button
#-------------------------------------------------------------
driver.get("https://www.myntra.com")
time.sleep(3)
abs_xpath = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div[2]/div[2]/div[2]/div[2]/span[1]")
print("Myntra Login Button (Absolute XPath):", abs_xpath.text)
rel_xpath = driver.find_element(By.XPATH, "//span[text()='Profile']")
print("Myntra Login Button (Relative XPath):", rel_xpath.text)

#-------------------------------------------------------------
# Task 4: BookMyShow 'Book Tickets' Button
#-------------------------------------------------------------

driver.get("https://in.bookmyshow.com")
time.sleep(3)
try:
    book_button = driver.find_element(By.CSS_SELECTOR, "button[class*='book-button']")
    print("BookMyShow Button (CSS):", book_button.text)
except:
    print("Book Tickets button appears only after selecting a showtime.")

#-------------------------------------------------------------
# Task 5: Dynamic Element Example (Amazon Add to Cart)
#-------------------------------------------------------------
driver.get("https://www.amazon.in")
time.sleep(3)
try:
    add_to_cart = driver.find_element(
        By.XPATH,
        "//span[text()='Apple iPhone']/ancestor::div[@data-component-type='s-search-result']//following-sibling::div//input[@value='Add to Cart']"
    )
    print("Add to Cart Button (XPath):", add_to_cart.get_attribute("outerHTML"))
except:
    print("Dynamic Add to Cart example depends on product availability.")

driver.quit()
