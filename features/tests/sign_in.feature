# Created by jacki at 3/14/2025
Feature: Target sign in test cases

  Scenario: Verify Sign In form opened
    Given Open target main page
    When Click sign in
    And Click side menu sign in
    Then Verify Sign In form opened