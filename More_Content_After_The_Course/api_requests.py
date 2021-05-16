import requests
import json
url = requests.get("https://www.python.org/")
print(url.status_code)

if url:
    print("The page loaded")
else:
    print("Response failed")
    
print(url.text)
json_element =json.dumps(url.text)
print(json_element)
print(url.headers)
print(url.headers["Date"])