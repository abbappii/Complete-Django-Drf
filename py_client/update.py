import requests

endpoint = "http://127.0.0.1:8000/api/products/5/update/"

data = {
    'title': 'this field update form update py file',
    'price': 35
}

get_response= requests.put(endpoint, json=data)

print(get_response.json())