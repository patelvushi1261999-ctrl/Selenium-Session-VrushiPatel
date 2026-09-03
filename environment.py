# import time
#
# from selenium import webdriver
# def before_scenario(context,scenario):
#     print("opening browser")
#     context.driver=webdriver.Chrome()
#     context.driver.maximize_window()
# def after_step(context,step):
#     time.sleep(3)
# def after_scenario(context,scenario):
#     print("closing browser")
#     context.driver.quit()
#
import os

def before_scenario(context, scenario):
    print(f"\n--- Starting scenario: {scenario.name} ---")

def after_scenario(context, scenario):
    print(f"--- Finished scenario: {scenario.name} ---\n")

def after_step(context, step):
    if step.status == "failed":
        # If you have a Selenium driver attached to context, capture screenshot
        if hasattr(context, "driver"):
            filename = f"screenshot_{scenario.name}_{step.name}.png"
            safe_filename = filename.replace(" ", "_").replace("/", "_")
            context.driver.save_screenshot(safe_filename)
            print(f"Screenshot saved: {safe_filename}")
