@hotel
Feature: Create hotel

  Scenario: If a hotel with the same name already exists, returns error
    Given hotel with uuid f3af7604-8410-45a0-9628-be125cac516d exists with values
    """json
    {
      "name": "Hotel Vela"
    }
    """
    When I make a POST request to /api/hotels/scrape with body
    """json
    {
      "name": "Hotel Vela"
    }
    """
    Then the response status code is 400
    And the response message is Hotel with name Hotel Vela already exists

  Scenario: Creates the hotel with the given name
    When I make a POST request to /api/hotels/scrape with body
    """json
    {
      "name": "Hotel Vela"
    }
    """
    Then the response status code is 200
    And exists a hotel with name Hotel Vela
