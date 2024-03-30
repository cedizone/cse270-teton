import pytest
import requests

def test_get_users_with_valid_credentials(mocker):
    url = "https://127.0.0.1:8000/users"
    params = {'username': 'admin', 
              'password': 'qwerty'
    }

    mocked_response = mocker.Mock()
    mocked_response.status_code = 200
    mocked_response.text = ''

    mocker.patch('requests.get', return_value=mocked_response)
    
    
    # Make a GET request with parameters
    response = requests.get(url, params=params)
    
    # Assert the HTTP status code and empty response body for the first test scenario
    assert response.status_code == 200
    assert response.text.strip() == ''


def test_get_users_with_invalid_credentials(mocker):
    url = "https://127.0.0.1:8000/users"
    params = {'username': 'admin', 'password': 'admin'}


    mocked_response = mocker.Mock()
    mocked_response.status_code = 401
    mocked_response.text = ''

    mocker.patch('requests.get', return_value=mocked_response)
    
    # Make a GET request with parameters for the second test scenario
    response = requests.get(url, params=params)
    
    # Assert the HTTP status code and that the response body contains the expected text
    assert response.status_code == 401
    assert response.text.strip() == ''
