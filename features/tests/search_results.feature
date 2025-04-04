# Created by jacki at 3/13/2025
Feature: Target search test cases

  Scenario: User can search for tea on Target
    Given Open target main page
    When Search for tea
    Then Verify correct search results shown for tea
    And Verify tea in URL

#  Scenario: User can search for a iPhone on Target
#    Given Open target main page
#    When Search for iPhone
#    Then Verify correct search results shown for iPhone
#
#  Scenario: User can search for a dress on Target
#    Given Open target main page
#    When Search for dress
#    Then Verify correct search results shown for dress

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

  Scenario: Verify that user can see product names and images
    Given Open target main page
    When Search for AirPods (3rd Generation)
    Then Verify that every product has a name and an image

  Scenario: User can see favorites tooltip for search results
    Given Open Target main page
    When Search for tea
    And Hover favorites icon
    Then Favorites tooltip is shown