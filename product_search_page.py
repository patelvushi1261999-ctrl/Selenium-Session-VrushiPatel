from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class ProductSearchPage:
    SEARCH_BOX = (By.NAME, "q")
    SEARCH_RESULTS = (By.CSS_SELECTOR, "div._4rR01T, a.s1Q9rs")

    def __init__(self, driver):
        self.driver = driver

    def enter_search_term(self, term):
        search_box = self.driver.find_element(*self.SEARCH_BOX)
        search_box.clear()
        search_box.send_keys(term)

    def submit_search(self):
        search_box = self.driver.find_element(*self.SEARCH_BOX)
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)

    def get_search_results(self):
        return self.driver.find_elements(*self.SEARCH_RESULTS)
