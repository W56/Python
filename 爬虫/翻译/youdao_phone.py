import requests
import json
from lxml import etree

url = "https://m.youdao.com/translate"

headers = {"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1","Referer": "https://m.youdao.com/translate"}

content = input("请输入想要翻译的内容：（自动检测）")

data = {"inputtext": content,"type": "AUTO"}

response = requests.post(url,data=data,headers=headers)

html_str = response.content.decode()

html = etree.HTML(html_str)

result = html.xpath("//div[@id='bd']//div[@class='generate']/ul/li/text()")[0]

print("翻译结果是：",result)