@hotel
Feature: Remove hotel

  Scenario: If the hotel exists, it is removed
    Given hotel with uuid f3af7604-8410-45a0-9628-be125cac516d exists with values
    """json
    {}
    """
    When I make a DELETE request to /api/hotels/f3af7604-8410-45a0-9628-be125cac516d
    Then the response status code is 200
    And a hotel with uuid f3af7604-8410-45a0-9628-be125cac516d does not exist

  Scenario: If the hotel does not exist, returns error
    When I make a DELETE request to /api/hotels/f3af7604-8410-45a0-9628-be125cac516d
    Then the response status code is 404
    And the response message is Hotel with uuid f3af7604-8410-45a0-9628-be125cac516d not found
