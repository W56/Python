import time,json,hashlib,random
import requests
content = input("请输入要翻译的内容：")

# url里面有个_o,不去掉会报错
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}

u = 'fanyideskweb'
d = content
f = str(int(time.time()*1000) + random.randint(1,10))
c = 'rY0D^0\'nM0}g5Mm1z%1G4'

data = {}

sign=hashlib.md5((u+d+f+c).encode('utf-8')).hexdigest()
#引号内容为固定
data['i']=content#需要翻译的内容
data['from'] = 'AUTO'
data['to'] = 'AUTO'
data['smartresult'] = 'dict'
data['client'] = 'fanyideskweb'
data['salt'] = f
data['sign'] = sign
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'FY_BY_CL1CKBUTTON'
data['typoResult'] = 'true'


reponse = requests.post(url,headers=headers,data=data)

res = reponse.content.decode()

res = json.loads(res)
print("翻译结果是：",res['translateResult'][0][0]['tgt'])