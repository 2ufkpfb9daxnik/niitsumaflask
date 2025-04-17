
<!-- saved from url=(0052)http://10.133.2.200/webprog/dyn/examples/bssample.py -->
<html><head><meta http-equiv="Content-Type" content="text/html; charset=Shift_JIS"></head><body>from bs4 import BeautifulSoup
html = """

    
        <title>貂&#65533;ｰｴ鄒ｩ蟄昴&#65533;闡玲嶌</title>
    
    
        <p class="title">
            <b>貂&#65533;ｰｴ鄒ｩ蟄昴&#65533;譛譁ｰ縺ｮ闡玲嶌縺ｫ縺ｯ縲∵ｬ｡縺ｮ譛ｬ縺後≠繧翫∪縺吶&#65533;</b>
        </p>
        <p class="recent books">
            <a class="book" href="https://www.amazon.co.jp/dp/B07TN4D3HG" id="link1">
                Python3縺ｫ繧医ｋ繝薙ず繝阪せ縺ｫ蠖ｹ遶九▽繝&#65533;&#65533;繧ｿ蛻&#65533;梵蜈･髢
            </a>
            <a class="book" href="http://www.amazon.co.jp/dp/B07SRLRS4M" id="link2">
                繧医￥繧上°繧輝ython3蜈･髢2.NumPy繝ｻMatplotlib邱ｨ
            </a>
            <a class="book" href="http://www.amazon.co.jp/dp/B07T9SZ96B" id="link3">
                繧医￥繧上°繧輝ython3蜈･髢4.Pandas縺ｧ繝&#65533;&#65533;繧ｿ蛻&#65533;梵邱ｨ
            </a>
        </p>
        <p class="end">
            <b>縺昴＠縺ｦ縲√％繧後ｉ縺ｮ譛ｬ縺ｯ螂ｽ隧慕匱螢ｲ荳ｭ縺ｧ縺吶&#65533;</b>
        </p>
    

"""
soup = BeautifulSoup(html,'html.parser')

## 蝓ｺ遉守噪縺ｪ菴ｿ縺&#65533;婿縲螳溯｡後＠縺ｦ縺昴ｌ縺槭ｌ縺ｮ蜃ｺ蜉帙ｒ遒ｺ隱阪＠縺ｦ縺ｿ繧医≧


print(soup.get_text())

print('--')

print(soup.html.head.title)

print('--')

print(soup.title)

print('--')

print(soup.title.string)

print('--')


for p in soup.body.find_all("p"):
    print(p)

print('--')


print(soup.body.p["class"])

print('--')


for child in soup.body.contents:
    print(child)

print('--')


print(soup.select(".end"))

print('--')


print(soup.select("p.end"))

print('--')
	
print(soup.select(".recent.books"))

print('--')

print(soup.select("#link2"))

print('--')

print(soup.select('a[href*="amazon"]'))

print('--')

print(soup.select("body &gt; p.end"))

print('--')



## 蠢懃畑萓&#65533;

## <p> 縺ｧ縲#link2 縺ｮ縺ゅｋ隕∫ｴ&#65533;縺ｮ隕ｪ隕∫ｴ&#65533;
for p in soup.body.find_all("p"):
    ret=p.select("#link2")
    if len(ret)&gt;0:
        print(ret[0].parent)
</p></body></html>