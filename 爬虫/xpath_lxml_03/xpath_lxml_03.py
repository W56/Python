import requests
import json
from lxml import etree

pages = [(i - 1) * 25 for i in range(1, 12)]

url = "https://www.douban.com/doulist/110585733/?start={}&sort=seq&playable=0&sub_type="

url_list = []

for page in pages :
    url_list.append(url.format(page))

# print(url_list)

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"}

cnt = 1

for url in url_list:
    response = requests.get(url,headers=headers)
    html_str = response.content.decode()
    html = etree.HTML(html_str)
    div_list = html.xpath("//div[@class='article']/div[@class='doulist-item']")
    content_list = []
    for div in div_list:
        item = {}
        item["title"] = div.xpath(".//div[@class='title']/a/text()")[0].strip()
        item["url"] = div.xpath(".//div[@class='post']/a/@href")
        item["rating_num"] = div.xpath(".//div[@class='rating']/span[@class='rating_nums']/text()")
        item["comment_num"] = div.xpath(".//div[@class='rating']/span[3]/text()")
        item["detailed_info"] = div.xpath(".//div[@class='abstract']/text()")
        for i in range(len(item["detailed_info"])):
            item["detailed_info"][i] = item["detailed_info"][i].strip()
        with open("3.txt","a",encoding="utf-8") as f:
            f.write(json.dumps(item,ensure_ascii=False))
            f.write("\n")
    print("第{}页保存成功".format(cnt))
    cnt += 1
