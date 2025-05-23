# Created by jacki at 3/14/2025
Feature: Target sign in test cases

  Scenario: Verify Sign In form opened
    Given Open target main page
    When Click sign in
    And Click side menu sign in
    Then Verify Sign In form opened

  Scenario: User can open and close Terms and Conditions from sign in page
    Given Open sign in page
    And Store original window
    When Click sign in
    And Click side menu sign in
    And Click on Target terms and conditions link
    And Switch to new window
    Then Verify Terms and Conditions page is opened
    And Close current page
    And Return to original window

  Scenario: Verify incorrect password fails to login
    Given Open sign in page
    When Click sign in
    And Click side menu sign in
    And Enter correct email: misepad562@ptiong.com
    And Click continue
    And Enter incorrect password: Password1234
    And Click Sign in button
    Then Verify error message is shown