import os
import sys
import requests
import json

# Ensure package imports work when running this file directly.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config.config import base_url, auth_token
from utils.helpers import generate_random_email


#GET Request
def get_request():
    url = base_url + "/public/v2/users"
    print("get url: " + url)
    headers = {"Authorization": auth_token}
    response = requests.get(url, headers=headers)
    print(response.status_code)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json GET response body: ", json_str)
    print(".......GET USER IS DONE.......")
    print(".......=====================.......")
    
#unauthorized token
def invalid_token():
    url = base_url + "/public/v2/users"
    print("invalid bearer token.......")
    headers = {"Authorization": "bearer auth token"}
    
    response = requests.get(url, headers = headers)
    print("response",  response.text)
    assert response.status_code == 401
    print("Invvalid token passed....")
    

#POST Request
def post_request():
    url = base_url + "/public/v2/users"
    print("post url: " + url)
    headers = {"Authorization": auth_token}
    data = {
        "name": "Neha Kashyap",
        "email": generate_random_email(),
        "gender": "Female",
        "status": "Inactive"
    }
    response = requests.post(url, json=data, headers=headers)
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json POST response body: ", json_str)
    user_id = json_data["id"]
    print("user id ===>", user_id)
    assert response.status_code == 201
    assert "name" in json_data
    assert json_data["name"] == "Neha Kashyap"
    print(".......POST/Create USER IS DONE.......")
    print(".......=====================.......")
    response = requests.get(url, headers=headers)
    print(response.status_code)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json GET response body: ", json_str)

    return user_id


#PUT Request
def put_request(user_id):
    url = base_url + f"/public/v2/users/{user_id}"
    print("PUT url: " + url)
    headers = {"Authorization": auth_token}
    data = {
        "name": "Neha Kashyap is trying this script",
        "email": generate_random_email(),
        "gender": "Female",
        "status": "active"
    }
    response = requests.put(url, json=data, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json PUT response body: ", json_str)
    assert json_data["id"] == user_id
    assert json_data["name"] == "Neha Kashyap is trying this script"
    print(".......PUT/Update USER IS DONE.......")
    print(".......=====================.......")

#Create user without email    
def post_user_without_email():
    url = base_url + "/public/v2/users"
    print("Create user without email....")
    headers = {"Authorization": auth_token}

    data = {
        "name": "Test User",
        "gender": "male",
        "status": "active"
    }

    response = requests.post(url, json=data, headers=headers)

    print("Response:", response.text)
    assert response.status_code == 422

    print(".......NEGATIVE TEST (NO EMAIL) PASSED.......")
    print(".......=====================.......")


#GET Single user details
def get_single_user(user_id):
    url = base_url + f"/public/v2/users/{user_id}"
    print("GET Single user url:" + url)
    headers = {"Authorization": auth_token}
    response = requests.get(url, headers=headers)
    print(response.status_code)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("Single user details:", json_str)
    assert json_data["id"] == user_id
    print(".......single user detail is visible.....")
    return user_id

#get invalid user 
def invalid_user(invalid_id):
    
    # url = base_url + f"/public/v2/users/{invalid_id}"
    url = base_url + f"/public/v2/users/{invalid_id}"

    print("Get invalid user details...........")
    headers = {"Authorization": auth_token}
    
    response = requests.get(url, headers = headers)
    
    print(response.status_code)
    assert response.status_code == 404
    
    print("Invalid user test passed....")
    return(invalid_id)
    

#Check response time 
def response_time():
    url = base_url + f"/public/v2/users"
    headers = {"Authorization": auth_token}
    response = requests.get(url, headers=headers)
    response_time = response.elapsed.total_seconds()
    print("Response Time:", response_time)

    assert response_time < 2
    print(".......RESPONSE TIME TEST PASSED.......")
    

    

#DELETE Request
# def delete_request(user_id):
    # url = base_url + f"/public/v2/users/{user_id}"
    # print("DELETE url: " + url)
    # headers = {"Authorization": auth_token}
    # response = requests.delete(url, headers=headers)
    # assert response.status_code == 204
    # print(".......DELETE USER IS DONE.......")
    # print(".......=====================.......")
    

#call
get_request()
invalid_token()
user_id = post_request()
put_request(user_id)
post_user_without_email()
invalid_user(555)
get_single_user(user_id)
response_time()
# delete_request(user_id)
print("All tests are done....")
