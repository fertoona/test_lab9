import requests
import pytest

@pytest.fixture
def response():
    headers={"x-api-key":"reqres_8c6ab82316cf4665b48079afa0450817"}
    data={"email":"mary.lig@mail.ru", "first_name":"Mary", "last_name":"Loginova", "avatar":"avatar"}
    r = requests.put("https://reqres.in/api/users/2",headers=headers,data=data)
    yield r

def test_status_200(response):
    assert response.status_code == 200

