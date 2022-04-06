import requests

endpoint = "http://127.0.0.1:8000/api/products/1"

data = {
    'title': 'this is new field',
    'price': 50
}

get_response= requests.get(endpoint, json=data)

print(get_response.json())