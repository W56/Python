import requests
import json

url = "https://read.douban.com/j/index//charts?type=highly_rated_sales&index=ebook&verbose=1"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"}

response = requests.get(url,headers=headers)

dict_data = json.loads(response.content.decode())

with open("douban_reading.txt","w",encoding="utf-8") as f:
    f.write(json.dumps(dict_data,ensure_ascii=False,indent=2))