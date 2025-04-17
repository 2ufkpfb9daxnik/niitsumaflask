import requests
from bs4 import BeautifulSoup

url="https://auctions.yahoo.co.jp/search/search?p=silver&exflg=1&b=51&n=50"
response = requests.get(url)
soup = BeautifulSoup(response.text)
rets = soup.find_all('a')
for x in rets:
    print(x)
