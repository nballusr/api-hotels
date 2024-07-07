@hotel
Feature: Create hotel

  Scenario: Creates the hotel with the given name
    When I make a POST request to /api/hotels/scrape with body
    """json
    {
      "name": "Hotel Vela"
    }
    """
    Then the response status code is 200
