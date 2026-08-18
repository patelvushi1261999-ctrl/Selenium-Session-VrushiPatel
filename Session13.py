#Task 1 -----------------------------------------------------------------------------------------------------
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.myntra.com/")
time.sleep(5)

actions = ActionChains(driver)
profile_actions = driver.find_element(By.XPATH, "//span[text()='Profile']")
actions.move_to_element(profile_actions).perform()
time.sleep(5)

dropdown = driver.find_element(By.XPATH, "//div[@class='desktop-user']")
print("Dropdown visible:", dropdown.is_displayed())


#Task 2 -----------------------------------------------------------------------------------------------------

driver.get("file:///C:/Users/vrush/Desktop/demo_spotify.html")
time.sleep(2)

actions = ActionChains(driver)

song = driver.find_element(By.ID, "song1")
playlist = driver.find_element(By.ID, "playlist")

actions.drag_and_drop(song, playlist).perform()
time.sleep(2)

print("Song dragged into playlist successfully.")

#task3-----------------------------------------------------------------------------------------------------

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("file:///C:/Users/vrush/Desktop/demo_flipkart.html")
time.sleep(2)

actions = ActionChains(driver)

product_img = driver.find_element(By.CLASS_NAME, "product-image")
actions.context_click(product_img).perform()
time.sleep(2)

wishlist_option = driver.find_element(By.XPATH, "//li[text()='Add to Wishlist']")
wishlist_option.click()
time.sleep(2)

print("Product added to wishlist successfully.")

#Task 4---------------------------------------------------------------------------------------


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("file:///C:/Users/vrush/Desktop/demo_spotify.html")
time.sleep(2)

actions = ActionChains(driver)

song = driver.find_element(By.ID, "song1")
playlist = driver.find_element(By.ID, "playlist")

actions.drag_and_drop(song, playlist).perform()
time.sleep(2)

print("Song dragged into playlist successfully.")

#Task 5-----------------------------------------------------------------------------------------
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("file:///C:/Users/vrush/Desktop/demo_zomato.html")  # replace with your file path
time.sleep(2)

search_box = driver.find_element(By.ID, "searchBox")
search_box.send_keys("Pizza Hut Vadodara")
time.sleep(2)

# Use keyboard actions to clear (without clear())
search_box.send_keys(Keys.CONTROL, "a")
search_box.send_keys(Keys.DELETE)
time.sleep(2)

print("Search box cleared:", search_box.get_attribute("value") == "")

driver.quit()