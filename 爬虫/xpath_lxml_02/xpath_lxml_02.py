import requests
import json
from lxml import etree

# 1.获取url地址
url = "https://www.douban.com/doulist/110585733/"

# 2.发送请求，获取响应
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"}
response = requests.get(url,headers=headers)

# 3.利用lxml模块
html_str = response.content.decode()
html = etree.HTML(html_str)

url_list = html.xpath("//div[@class='article']/div[@class='doulist-item']//div[@class='title']/a/text()")

for i in range(len(url_list)):
    url_list[i] = url_list[i].strip()
    with open("2.txt","a",encoding="utf-8") as f:
        f.write(json.dumps(url_list[i],ensure_ascii=False))
        f.write("\n")

