# Created by jacki at 3/16/2025
Feature: Main page ui test

  @smoke
  Scenario: Verify header links are shown
    Given  Open target main page
    Then Verify 6 header links are shown