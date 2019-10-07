Feature: Hello
    A site where you can save and display greetings.

Scenario: Create a greeting
    Given I am on the grettings page
    When I enter a greeing in the input
    And I press the save button
    Then I should see the new message displayed below
