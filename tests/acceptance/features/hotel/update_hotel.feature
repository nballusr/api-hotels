@hotel
Feature: Update hotel

  Scenario: If the hotel exists, it is updated
    Given hotel with uuid f3af7604-8410-45a0-9628-be125cac516d exists with values
    """json
    {
      "name": "Prev name",
      "location": "Prev location",
      "description": "Prev description",
      "has_swimming_pool": false
    }
    """
    When I make a PUT request to /api/hotels/f3af7604-8410-45a0-9628-be125cac516d with body
    """json
    {
      "name": "Hotel Vela",
      "location": "C/ Barcelona",
      "description": "Beautiful",
      "has_swimming_pool": true
    }
    """
    Then the response status code is 200
    And exists a hotel with uuid f3af7604-8410-45a0-9628-be125cac516d and values
    """json
    {
      "name": "Hotel Vela",
      "location": "C/ Barcelona",
      "description": "Beautiful",
      "has_swimming_pool": true
    }
    """

  Scenario: If the hotel does not exist, returns error
    When I make a PUT request to /api/hotels/f3af7604-8410-45a0-9628-be125cac516d with body
    """json
    {
      "name": "Hotel Vela",
      "location": "C/ Barcelona",
      "description": "Beautiful",
      "has_swimming_pool": true
    }
    """
    Then the response status code is 404
    And the response message is Hotel with uuid f3af7604-8410-45a0-9628-be125cac516d not found
