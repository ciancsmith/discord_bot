import requests
import json

response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
    headers={'Accept': 'application/vnd.github.v3.text-match+json'},
)
json_response = response.json()

r = requests.post('https://httpbin.org/post', data=json_response)
j = response.json()
print(j)
