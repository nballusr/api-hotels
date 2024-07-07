@hotel
Feature: Get hotels

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
    And hotel with uuid 7ee6c704-dc9e-44c3-b51d-58dd59f273e9 exists with values
    """json
    {
      "name": "Hotel Navarro",
      "location": "C/ Mallorca",
      "description": "Acceptable",
      "has_swimming_pool": false
    }
    """
    When I make a GET request to /api/hotels
    Then the response status code is 200
    And the JSON node hotels should have 2 elements
    And the JSON node hotels.0.uuid should be f3af7604-8410-45a0-9628-be125cac516d
    And the JSON node hotels.0.name should be Hotel Vela
    And the JSON node hotels.0.location should be C/ Barcelona
    And the JSON node hotels.0.description should be Beautiful
    And the JSON node hotels.0.has_swimming_pool should be true
    And the JSON node hotels.1.uuid should be 7ee6c704-dc9e-44c3-b51d-58dd59f273e9
    And the JSON node hotels.1.name should be Hotel Navarro
    And the JSON node hotels.1.location should be C/ Mallorca
    And the JSON node hotels.1.description should be Acceptable
    And the JSON node hotels.1.has_swimming_pool should be false

  Scenario: If there are no hotels, empty list is returned
    When I make a GET request to /api/hotels
    Then the response status code is 200
    And the JSON node hotels should have 0 elements
