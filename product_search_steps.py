from behave import given, when, then
from selenium import webdriver
from features.pages.product_search_page import ProductSearchPage

@given("the user launches the browser")
def step_launch_browser(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()

@given("navigates to the Flipkart homepage")
def step_open_homepage(context):
    context.driver.get("https://www.flipkart.com")
    context.search_page = ProductSearchPage(context.driver)

@when('the user enters "{product}" in the search bar')
def step_enter_product(context, product):
    context.search_page.enter_search_term(product)

@when("clicks the search button")
def step_click_search(context):
    context.search_page.submit_search()

@then('the search results should display products related to "{product}"')
def step_verify_results(context, product):
    results = context.search_page.get_search_results()
    assert len(results) > 0, f"No results found for {product}"
    print(f"Found {len(results)} results for {product}")
    context.driver.quit()
