# Python strip()方法

## 描述

Python strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。  
<br/>
**注意**：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。

## 语法
```python
str.strip([chars]);
```

## 参数
chars -- 移除字符串头尾指定的字符序列。  
<br/>

## 返回值
返回移除字符串头尾指定的字符生成的新字符串。

## 实例
```python
>>> str = "         \n    123        "
>>> new_str = str.strip()
>>> new_str
'123'

>>> str = "123abcdefg123"
>>> new_str = str.strip("123")
>>> new_str
'abcdefg'
```