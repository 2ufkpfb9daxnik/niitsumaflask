import requests
from bs4 import BeautifulSoup
import urllib.parse

s_quote = urllib.parse.quote("銀製品")
#print(s_quote)
url="https://auctions.yahoo.co.jp/search/search?p="+
s_quote + "&exflg=1&b=51&n=50"
response = requests.get(url)
soup = BeautifulSoup(response.text)
rets = soup.find_all('a')
for x in rets:
    print(x)
