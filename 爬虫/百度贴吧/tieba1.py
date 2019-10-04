import re
import requests
import urllib
from retrying import retry

'''
注意：
1. while循环的结束条件
2. 使用正则表达式
3. urllib.request.urlretrieve，当前路径下的picture文件夹一定要存在，否则会报错
'''


class TieBaSpider():

    def __init__(self):
        self.temp_url = "http://tieba.baidu.com/p/6024122230?pn={}"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"}

    @retry(stop_max_attempt_number = 3)
    def _parse_url(self,url):
        response = requests.get(url,self.headers,timeout=3)
        return response.content.decode()

    def parse_url(self,url):
        try:
            html_str = self._parse_url(url)
        except:
            html_str = None

        return html_str

    def run(self):

        page = 1
        cnt = 1

        while page<=11:
            # 1.url
            url = self.temp_url.format(page)

            # 2.发送请求获取响应
            html_str = self.parse_url(url)

            # 3.提取数据
            reg = r"http://imgsrc.baidu.com/forum/w%3D580/sign=.+?\.jpg"
            picture_list = re.findall(reg, html_str)

            # 4.保存数据
            for pic in picture_list:
                urllib.request.urlretrieve(pic, "./picture/%s.jpg" % cnt)
                cnt += 1
            print("第{}页图片保存成功".format(page))
            print(url)
            page += 1

if __name__ == '__main__':
    tieba = TieBaSpider()
    tieba.run()
