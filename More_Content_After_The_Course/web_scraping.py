import bs4
import urllib.request
#url = 'https://www.amazon.com'
url = "https://www.walmart.com/ip/Heypex-Global-Earloop-Disposable-Face-Masks-50ct/509796009?wpa_bd=&wpa_pg_seller_id=4B5771C055E24182BF23461BB6B23B0B&wpa_ref_id=wpaqs:1mJkyq2rXQi55AX6WGOKzxlaSsVbKuIDqdGqTBpJ9O437h3r0Mzyjd-uOICPXSWR9renAuZWM6QZ32513Gz7ydrgI8n19Qw9ZvPfCXvIci6vD0KEDsWDCgdvDDaeusZoS3KJ99kuOoWiPmv0bPOmqTw8CjubweEIeHmWtSGX5lXRTDjhYNlN0s8HgBA-p96czvutgEcxFvKSYet36H1sSQ&wpa_tag=&wpa_aux_info=&wpa_pos=3&wpa_plmt=1145x1145_T-C-IG_TI_1-6_HL-INGRID-GRID-NY&wpa_aduid=22e097d4-199c-4fed-af3d-9fc9e76b846c&wpa_pg=search&wpa_pg_id=face%20mask&wpa_st=face%2Bmask&wpa_tax=5438_1045799_2363684&wpa_bucket=__bkt__"
sauce = urllib.request.urlopen(url).read()
soup = bs4.BeautifulSoup(sauce, "html.parser")

prices = soup.find(id = "price")
print(prices)
#print(soup.prettify())