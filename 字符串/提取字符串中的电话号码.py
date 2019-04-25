#使用正则表达式提取字符串中的电话号码

import re

telNumber = """Suppose my Phone No. is 0525-1234567, yours is 010-12345678, his is
025-87654321 
"""
pattern = re.compile(r'(\d{3,4})-(\d{7,8})')

index = 0

while True:
    matchResult = pattern.search(telNumber,index) #从指定位置开始匹配
    if not matchResult:
        break
    print('-'*30)
    print('Success:')
    for i in range(3):
        print('Search Content:',matchResult.group(0),
              'Start from:',matchResult.start(i),'End at:',matchResult.end(i),
              'Its span is:',matchResult.span(i))

    index = matchResult.end(2)

'''
运行结果：
------------------------------
Success:
Search Content: 0525-1234567 Start from: 24 End at: 36 Its span is: (24, 36)
Search Content: 0525-1234567 Start from: 24 End at: 28 Its span is: (24, 28)
Search Content: 0525-1234567 Start from: 29 End at: 36 Its span is: (29, 36)
------------------------------
Success:
Search Content: 010-12345678 Start from: 47 End at: 59 Its span is: (47, 59)
Search Content: 010-12345678 Start from: 47 End at: 50 Its span is: (47, 50)
Search Content: 010-12345678 Start from: 51 End at: 59 Its span is: (51, 59)
------------------------------
Success:
Search Content: 025-87654321 Start from: 68 End at: 80 Its span is: (68, 80)
Search Content: 025-87654321 Start from: 68 End at: 71 Its span is: (68, 71)
Search Content: 025-87654321 Start from: 72 End at: 80 Its span is: (72, 80)
'''
