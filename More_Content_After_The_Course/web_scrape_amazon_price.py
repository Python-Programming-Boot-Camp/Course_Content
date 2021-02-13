import requests
from bs4 import BeautifulSoup
URL = 'https://ndsmcobserver.com/'
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"}
page = requests.get(URL, headers=headers)
soup = BeautifulSoup (page.content, 'html.parser')
title = soup.find(id="line")
print(title)