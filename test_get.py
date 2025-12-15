import requests
import pytest

@pytest.fixture
def response():
    r = requests.get("https://reqres.in/api/users/2",headers={"x-api-key":"reqres_8c6ab82316cf4665b48079afa0450817"})
    yield r

def test_status_200(response):
    assert response.status_code == 200

def test_response_data(response):
    jsonData = response.json()
    assert jsonData.get("data")
    
def test_response_data_email(response):
    jsonData = response.json()
    data = jsonData.get("data")
    assert "@reqres.in" in data.get("email") 

def test_response_data_first_name(response):
    jsonData = response.json()
    data = jsonData.get("data")
    assert data.get("first_name") == "Janet"