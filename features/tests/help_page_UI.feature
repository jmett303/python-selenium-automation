# Created by jacki at 3/16/2025
Feature: Target help page UI Test Cases

  Scenario: Target Help Header present on Help page
    Given Open target help page
    Then Verify Help Header present on page

  Scenario: Search box present on Help page
    Given Open target help page
    Then Verify search box present on page

  Scenario: Help options present on Help page
    Given Open target help page
    Then Verify Help options present on page