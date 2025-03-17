# Created by jacki at 3/13/2025
Feature: Cart tests

  Scenario: 'Your cart is empty' message is shown for empty cart
    Given Open target main page
    When Click on cart icon
    Then verify 'Your cart is empty' message is shown

