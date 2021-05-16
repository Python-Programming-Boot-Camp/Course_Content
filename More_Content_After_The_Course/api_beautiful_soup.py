import requests
from bs4 import BeautifulSoup
url = "https://finance.yahoo.com/quote/%5EDJI/"
response = requests.get(url)
print(response.text)