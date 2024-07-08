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

  Scenario: If another hotel with same name exists, returns error
    Given hotel with uuid f3af7604-8410-45a0-9628-be125cac516d exists with values
    """json
    {
      "name": "Prev name",
      "location": "Prev location",
      "description": "Prev description",
      "has_swimming_pool": false
    }
    """
    And hotel with uuid df699b63-0cdb-4c2e-b42d-6422a8a24400 exists with values
    """json
    {
      "name": "Hotel Vela",
      "location": "Another location",
      "description": "Another description",
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
    Then the response status code is 400
    And the response message is Hotel with name Hotel Vela already exists
