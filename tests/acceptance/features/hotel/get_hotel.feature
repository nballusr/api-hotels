@hotel
Feature: Get hotel

  Scenario: If the hotel exists, it is returned
    Given hotel with uuid f3af7604-8410-45a0-9628-be125cac516d exists with values
    """json
    {
      "name": "Hotel Vela",
      "location": "C/ Barcelona",
      "description": "Beautiful",
      "has_swimming_pool": true
    }
    """
    When I make a GET request to /api/hotels/f3af7604-8410-45a0-9628-be125cac516d
    Then the response status code is 200
    And the JSON node uuid should be f3af7604-8410-45a0-9628-be125cac516d
    And the JSON node name should be Hotel Vela
    And the JSON node location should be C/ Barcelona
    And the JSON node description should be Beautiful
    And the JSON node has_swimming_pool should be true

  Scenario: If the hotel does not exist, returns error
    When I make a GET request to /api/hotels/f3af7604-8410-45a0-9628-be125cac516d
    Then the response status code is 404
    And the response message is Hotel with uuid f3af7604-8410-45a0-9628-be125cac516d not found
