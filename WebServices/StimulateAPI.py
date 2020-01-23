import requests

import jsonpath

import json


baseURL="https://reqres.in/api/users?page=2"

response=requests.get(baseURL)

print(response.status_code)

if response.status_code==200:
    print("Service is up and running")
    print(response.content)
    data=json.loads(response.content)
    print(type(data))

    print(data['page'])
else:
    print("Service is not running")