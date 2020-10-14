import requests
import json


global HEADERS
HEADERS = {
    "Authorization": "basic T64Mdy7m[",
    "Content-Type" : "application/json; charset=utf-8",
    "credentials": "include",
    "Referer" : "https://opentimetable.dcu.ie/",
    "Origin" : "https://opentimetable.dcu.ie/"
}

response = requests.get("https://opentimetable.dcu.ie/broker/api/viewOptions", headers=HEADERS)
weeks = json.loads(response.text)['Weeks']
print(weeks)
#https://opentimetable.dcu.ie/broker/api/CategoryTypes/241e4d36-60e0-49f8-b27e-99416745d98d/Categories/Filter?pageNumber=1&query=CASE3

res = requests.post("https://opentimetable.dcu.ie/broker/api/CategoryTypes/1e042cb1-547d-41d4-ae93-a1f2c3d34538/Categories/Filter?pageNumber=1&query=LG25", headers=HEADERS)
print(res.text)