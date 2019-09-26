from lxml import etree
import requests
import json

url = "https://movie.douban.com/chart"

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"}

response = requests.get(url,headers=headers)

html_str = response.content.decode()

#print(response.content.decode())

html = etree.HTML(html_str)

#print(html)

name_list = html.xpath("//div[@class='indent']//table//div[@class='pl2']/a/text()")

url_list = html.xpath("//div[@class='indent']//table//div[@class='pl2']/a/@href")

actors_list = html.xpath("//div[@class='indent']//table//div[@class='pl2']/p/text()")

grades_list = html.xpath("//div[@class='indent']//table//div[@class='pl2']/div[@class='star clearfix']/span[@class='rating_nums']/text()")

# print(name_list)
# print(type(name_list))
# print(url_list)
# print(actors_list)
# print(grades_list)

new_name_list = []

for num in range(len(name_list)):
    temp = name_list[num].replace("/","").strip()
    if temp!="":
        new_name_list.append(temp)

item = {}

for num in range(len(new_name_list)):
    item["name"] = new_name_list[num]
    item["url"] = url_list[num]
    item["actors"] = actors_list[num]
    item["grade"] = grades_list[num]
    print(item)
    with open("1.txt","a",encoding="utf-8") as f:
        f.write(json.dumps(item,ensure_ascii=False))
        f.write("\n")
