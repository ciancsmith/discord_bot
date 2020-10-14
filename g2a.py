import requests
import bs4 as bs

res = requests.get("https://api.zilerate.com/amazon/deals?apiKey=https%3A%2F%2Fapi.zilerate.com%2Famazon%2Fbestsellers%3FapiKey%3DcOGwytQeXD9vefugIou0y847XZz3M9lE5Bil9Rib&includeHtml=true")
print(res.text)