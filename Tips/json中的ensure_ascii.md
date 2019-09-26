**JSON**(JavaScript Object Notation, JS 对象简谱) 是一种轻量级的数据交换格式。它基于 ECMAScript (欧洲计算机协会制定的js规范)的一个子集，采用完全独立于编程语言的文本格式来存储和表示数据。简洁和清晰的层次结构使得 JSON 成为理想的数据交换语言。 易于人阅读和编写，同时也易于机器解析和生成，并有效地提升网络传输效率。

在使用json.dumps()需要注意：

```python
>>> import json
>>> print(json.dumps("中国"))
"\u4e2d\u56fd"
```

这是因为json.dumps 序列化时对中文默认使用的ascii编码.想输出真正的中文需要指定ensure_ascii=False：

```python
>>> import json
>>> print(json.dumps("中国",ensure_ascii=False))
"中国"
```