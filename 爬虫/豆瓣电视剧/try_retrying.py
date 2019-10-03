import requests
from retrying import retry

'''
retrying模块的简单使用
@retry(stop_max_attempt_number=3)
'''

@retry(stop_max_attempt_number=3)
def _parse_url(url):
    print("*"*100)
    headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
               "Referer": "https://m.douban.com/tv/american"
               }
    response = requests.get(url,headers=headers,timeout=3)
    return response.content.decode()

def parse_url(url):
    try :
        html_str = _parse_url(url)
    except:
        html_str = None

    return html_str
