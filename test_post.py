import requests
import pytest

@pytest.fixture
def response():
    headers={"x-api-key":"reqres_8c6ab82316cf4665b48079afa0450817"}
    data={"email":"mary.lig@mail.ru", "first_name":"Mary", "last_name":"Loginova", "avatar":"avatar"}
    r = requests.post("https://reqres.in/api/users",headers=headers,data=data)
    yield r

def test_status_201(response):
    assert response.status_code == 201

def test_response_data_id(response):
    jsonData = response.json()
    assert jsonData.get("id") 