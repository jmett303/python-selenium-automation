# Created by jacki at 3/13/2025
Feature: Target search test cases

  Scenario: User can search for tea on Target
    Given Open target main page
    When Search for tea
    Then Verify correct search results shown for tea
    And Verify tea in URL


  Scenario Outline: User can search for a product on Target
    Given Open target main page
    When Search for <product>
    Then Verify correct search results shown for <expected_product>
    Examples:
    |product  |expected_product |
    |tea      |tea              |
    |iPhone   |iPhone           |
    |dress    |dress            |


  Scenario: Verify product added to cart
    Given Open target main page
    When Search for soda
    And Add to cart
    And Store product name
    And Confirm add to cart
    And Navigate to Cart
    Then Verify item added to cart
    Then Verify cart has correct product