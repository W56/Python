import json
import requests
from try_retrying import parse_url


class DoubanSpider():

    def __init__(self):
        self.temp_url = "https://m.douban.com/rexxar/api/v2/subject_collection/tv_american/items?os=ios&for_mobile=1&start={}&count=18&loc_id=108288&_=0"

    def get_content_list(self,html_str): #提取数据
        dict_data = json.loads(html_str)
        total = dict_data["total"]
        content_list = dict_data["subject_collection_items"]

        return content_list,total

    def save_content_list(self,content_list):
        for content in content_list:
            with open("douban.txt","a+",encoding="utf-8") as f:
                f.write(json.dumps(content,ensure_ascii=False))
                f.write("\n")
        print("保存成功")


    def run(self):
        # 1.url
        num = 0
        total = 10
        while num < total+18:
            url = self.temp_url.format(num)
            print(url)
            # 2.发送请求，获取响应
            html_str = parse_url(url)
            # 3.提取数据
            content_list,total = self.get_content_list(html_str)
            # 4.保存数据
            self.save_content_list(content_list)
            # 5.循环
            num += 18

if __name__ == '__main__':
    douban = DoubanSpider()
    douban.run()