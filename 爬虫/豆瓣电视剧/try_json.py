import requests
import json

url = "https://m.douban.com/rexxar/api/v2/subject_collection/tv_american/items?os=ios&for_mobile=1&start=0&count=18&loc_id=108288&_=0"

headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
    "Referer": "https://m.douban.com/tv/american"
}

response = requests.get(url,headers=headers)

html_str = response.content.decode()

html_str = json.loads(html_str)

with open("tv_american.txt","w",encoding="utf-8") as f:
    f.write(json.dumps(html_str,ensure_ascii=False,indent=2))