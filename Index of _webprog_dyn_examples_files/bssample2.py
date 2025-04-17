from bs4 import BeautifulSoup
html = """
<ul id="book">
  <li>Python3によるビジネスに役立つデータ分析入門</li>
  <li>よくわかるPython3入門1.基礎編</li>
  <li>よくわかるPython3入門2.NumPy・Matplotlib編</li>
  <li>よくわかるPython3入門4.Pandasでデータ分析編</li>
</ul>
"""
soup = BeautifulSoup(html,'html.parser')


print(soup.select("ul#book > li"))

print(soup.select("ul#book > li:nth-of-type(2)"))
