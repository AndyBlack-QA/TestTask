import requests
import pytest


HEADERS = {
    "x-api-key": "reqres-free-v1",
}

def test_create_user():
    payload = {
        "name": "morpheus",
        "job": "leader"
    }
    BASE_URL = "https://reqres.in/api/users"
    
    response = requests.post(BASE_URL, headers=HEADERS, json=payload)
    
    assert response.status_code == 201, f"Expected status code 201, but got {response.status_code}"
    
    response_data = response.json()
    assert response_data["name"] == "morpheus", f"Expected name 'morpheus', but got {response_data['name']}"
    assert response_data["job"] == "leader", f"Expected job 'leader', but got {response_data['job']}"
    assert "id" in response_data, "Response does not contain 'id'"
    assert "createdAt" in response_data, "Response does not contain 'createdAt'"


BASE_URL = "https://reqres.in/api/users/2"


def test_update_user():
    payload = {
        "name": "morpheus",
        "job": "zion resident"
    }
    
    response = requests.put(BASE_URL, headers=HEADERS, json=payload)
    
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    
    response_data = response.json()
    assert response_data["name"] == "morpheus", f"Expected name 'morpheus', but got {response_data['name']}"
    assert response_data["job"] == "zion resident", f"Expected job 'zion resident', but got {response_data['job']}"
    assert "updatedAt" in response_data, "Response does not contain 'updatedAt'"


def test_update_user_without_name():
    payload = {"job": "zion resident"}
    
    response = requests.put(BASE_URL, headers=HEADERS, json=payload)
    
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    response_data = response.json()
    assert response_data["job"] == "zion resident", f"Expected job 'zion resident', but got {response_data['job']}"
    assert "updatedAt" in response_data, "Response does not contain 'updatedAt'"


def test_patch_update_user():
    # Update user using patch method
    payload = {
        "name": "morpheus",
        "job": "zion resident"
    }

    response = requests.patch(BASE_URL, headers=HEADERS, json=payload)
    
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    
    response_data = response.json()
    assert response_data["name"] == "morpheus", f"Expected name 'morpheus', but got {response_data['name']}"
    assert response_data["job"] == "zion resident", f"Expected job 'zion resident', but got {response_data['job']}"
    assert "updatedAt" in response_data, "Response does not contain 'updatedAt'"


def test_delete_user():
    # Successful user deletion
    response = requests.delete(BASE_URL, headers=HEADERS)
    
    assert response.status_code == 204, f"Expected status code 204, but got {response.status_code}"


def test_delete_without_api_key():
    # 401 error when trying to delete user w/o API key
    response = requests.delete(BASE_URL)

    assert response.status_code == 401, f"Expected status code 401, but got {response.status_code}"


BASE_REGISTER_URL = "https://reqres.in/api/register"


def test_register_success():
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "JUNO"
    }

    response = requests.post(BASE_REGISTER_URL, headers=HEADERS, json=payload)
    
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    
    response_data = response.json()
    assert "id" in response_data, "Response does not contain 'id'"
    assert "token" in response_data, "Response does not contain 'token'"
    assert response_data["id"] == 4, f"Expected id 4, but got {response_data['id']}"
    assert response_data["token"] == "QpwL5tke4Pnpja7X4", f"Expected token 'QpwL5tke4Pnpja7X4', but got {response_data['token']}"


def test_register_missing_password():
    # 400 error if there is password when register user
    payload = {
        "email": "kva-kva@andrei.by"
    }

    response = requests.post(BASE_REGISTER_URL, headers=HEADERS, json=payload)
    
    assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"
    assert "error" in response.json(), "Response does not contain error message"


def test_register_missing_email():
    # 400 error if there is email when register user
    payload = {
        "password": "kva-kva"
    }

    response = requests.post(BASE_REGISTER_URL, headers=HEADERS, json=payload)
    
    assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"
    assert "error" in response.json(), "Response does not contain error message"


def test_register_invalid_email():
    # 400 error if email is invalid
    payload = {
        "email": "kva-kva",
        "password": "JUNO"
    }

    response = requests.post(BASE_REGISTER_URL, headers=HEADERS, json=payload)
    
    assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"
    assert "error" in response.json(), "Response does not contain error message"


