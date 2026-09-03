Feature: Flipkart-style product search

  Background:
    Given the user launches the browser
    And navigates to the Flipkart homepage

  Scenario: Search for a product by name
    When the user enters "Laptop" in the search bar
    And clicks the search button
    Then the search results should display products related to "Laptop"

  Scenario: Search for another product by name
    When the user enters "Shoes" in the search bar
    And clicks the search button
    Then the search results should display products related to "Shoes"

