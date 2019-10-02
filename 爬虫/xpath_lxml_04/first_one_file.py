import requests
from lxml import etree
import json

url = "https://www.python.org/dev/peps/pep-0020/"

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"}

response = requests.get(url,headers=headers)

html_str = response.content.decode()

html = etree.HTML(html_str)

title = html.xpath("//div[@id='the-zen-of-python']//a/text()")[0]

content = html.xpath("//div[@id='the-zen-of-python']/pre/text()")[0]

with open("The_Zen_of_Python.txt","a+",encoding="utf-8") as f:
    f.write(title)
    for line in content:
        f.write(line)

