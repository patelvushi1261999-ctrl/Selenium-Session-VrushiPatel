Task 2 --> Write a Selenium WebDriver script that opens the Myntra homepage, waits for 3 seconds, and then closes the browser window.<br><br><em><strong>Hint:</strong> Use driver.get('https://www.myntra.com') and a sleep/wait method before driver.quit().</em>





from selenium import webdriver

import time



\# Initialize Chrome WebDriver

driver = webdriver.Chrome()



\# Open Myntra homepage

driver.get("https://www.myntra.com")



\# Wait for 3 seconds

time.sleep(3)



\# Close the browser

driver.quit()





\-------------------------------------------------------------------------------------------------------------------------------------------

Task 3 --> Compare manual testing and automation testing by listing 3 scenarios from your daily-used apps (like Zomato, Instagram, or IRCTC) where automation would save time, and 2 scenarios where manual testing is still necessary.







Scenario									Automation Testing			Manual Testing

* Zomato - Search restaurants using different city names repeatedly	            Yes	
* Instagram - Login with multiple user accounts repeatedly		            Yes	
* IRCTC - Verify train search across many stations and dates			    Yes	
* Instagram - Check if the new user interface is visually attractive and easy to use					    Yes
* Zomato - Verify food images, colors, fonts, and overall user experience		  			            Yes



Why Automation Saves Time

1. Repeating the same login tests hundreds of times.
2. Running regression tests after every application update.
3. Testing the same functionality across different browsers.



Why Manual Testing is Necessary

1. Checking the application's look and feel (UI/UX).
2. Exploratory testing to discover unexpected issue

\-----------------------------------------------------------------------------------------------------------------------------------------



Task 4 --> Draw a simple diagram (hand-drawn or digital) showing how Selenium WebDriver communicates with browser drivers and browsers. Label each component and explain in 2-3 lines what role each plays in automation.



&#x20;             Test Script

&#x20;            (Python / Java)



&#x20;                    │

&#x20;                    ▼



&#x20;         Selenium WebDriver API



&#x20;                    │

&#x20;       Sends Commands (W3C Protocol)



&#x20;                    ▼



&#x20;         ChromeDriver (Browser Driver)



&#x20;                    │

&#x20;      Translates Commands to Chrome



&#x20;                    ▼



&#x20;            Google Chrome Browser





