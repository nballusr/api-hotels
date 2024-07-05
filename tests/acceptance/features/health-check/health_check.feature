Feature: can run HTTP API

  Scenario: make a sample request
    When I make a GET request to /api/health-check
    Then the response status code is 200

  Scenario: make a request to a non-existing endpoint
    When I make a GET request to /api/non-existing
    Then the response status code is 404
