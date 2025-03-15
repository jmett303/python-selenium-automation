# Created by jacki at 3/13/2025
Feature: Target search test cases

  Scenario Outline: User can search for a product on Target
    Given Open target main page
    When Search for <product>
    Then Verify correct search results shown for <expected_product>
    Examples:
    |product  |expected_product |
    |tea      |tea              |
    |iPhone   |iPhone           |
    |dress    |dress            |

#
#  Scenario: User can search for a iPhone on Target
#    Given Open target main page
#    When Search for iPhone
#    Then Verify correct search results shown for iPhone
#
#  Scenario: User can search for a dress on Target
#    Given Open target main page
#    When Search for dress
#    Then Verify correct search results shown for dress
