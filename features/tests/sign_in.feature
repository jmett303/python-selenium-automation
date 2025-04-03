# Created by jacki at 3/14/2025
Feature: Target sign in test cases

  Scenario: Verify Sign In form opened
    Given Open target main page
    When Click sign in
    And Click side menu sign in
    Then Verify Sign In form opened

  Scenario: User can open and close Terms and Conditions from sign in page
    Given Open sign in page
    When Store original window
    And Click on Target terms and conditions link (*see image below)
    And Switch to the newly opened window
    Then Verify Terms and Conditions page is opened
    And User can close new window and switch back to original