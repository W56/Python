import requests

url = "https://www.baidu.com/"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"}

response = requests.get(url,headers=headers)

# 发送请求的url地址
print("response.request.url:",response.request.url)

# 响应的url地址
print("response.url:",response.url)

# 请求头
print("response.request.headers:",response.request.headers)

# 响应头
print("response.headers:",response.headers)
