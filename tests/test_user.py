import pytest
import requests
import responses

@responses.activate
def test_get_users_with_invalid_credentials():
    url = "https://127.0.0.1:8000/users"
    params = {'username': 'admin', 'password': 'admin'}
    
    # Mock the server response for invalid credentials
    responses.add(responses.GET, url, json={}, status=401)
    
    # Make a GET request with parameters
    response = requests.get(url, params=params)
    
    # Assert the HTTP status code and empty response body for the first test scenario
    assert response.status_code == 401, "Expected HTTP status code 401 for unauthorized access"
    assert response.text == "{}", "Expected an empty response body for unauthorized access"

@responses.activate
def test_get_users_with_valid_credentials():
    url = "https://127.0.0.1:8000/users"
    params = {'username': 'admin', 'password': 'qwerty'}
    expected_response_text = "Access granted"
    
    # Mock the server response for valid credentials
    responses.add(responses.GET, url, body=expected_response_text, status=200)
    
    # Make a GET request with parameters for the second test scenario
    response = requests.get(url, params=params)
    
    # Assert the HTTP status code and that the response body contains the expected text
    assert response.status_code == 200, "Expected HTTP status code 200 for authorized access"
    assert response.text == expected_response_text, f"Expected response body to be '{expected_response_text}'"
