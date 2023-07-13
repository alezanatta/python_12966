import requests

response = requests.get("http://httpbin.org/status/429")

print(response)
