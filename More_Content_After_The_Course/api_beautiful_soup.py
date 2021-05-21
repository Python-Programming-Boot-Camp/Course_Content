import requests
from bs4 import BeautifulSoup
from time import sleep
#headers = {"User Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}
#print(response.text)
def stock_price():
    #url = "https://finance.yahoo.com/quote/%5EDJI/"
    url = "https://finance.yahoo.com/quote/YM%3DF?p=YM%3DF"
    response = requests.get(url)
    soup = BeautifulSoup(response.text,"html.parser")   
    price = soup.find("span",{"class":"Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"}).text
    return price
price = stock_price()
print("\nThe Dow Jones Industrial Average Future is: "+ str(price),end="")
while True:
    new_price = stock_price()
    if new_price != price:
        price = stock_price()
        #print("\nThe Dow Jones Industrial Average is:",price)
        print("\rThe Dow Jones Industrial Average Future is: "+ str(price),end="")
    sleep(1)
    