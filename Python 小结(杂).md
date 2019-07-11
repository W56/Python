# 标识符与保留字
- 保留字不可以当作标识符。
- 在特殊的编程语言里，这些保留字具有较为特殊的意义，并且在语言的说明格式里被预先定义。通常保留字包括用来支持类型系统的原始数据类型的标记，并可以用来识别诸如循环结构、语句块、条件、分支等程序结构。  
```python
import keyword
print(keyword.lwlist)
'''
输出结果：
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
'''
```
<br>

# Python 语言里常见的程序结构
1. 换行

2. 程序代码超过一行

3. 将数行表达式写成一行

4. 注释  
<br>

# 数据类型
Python3有6个标准的数据类型
1. Number （数字） int，float，bool，complex  
    在Python2中没有bool型，用数字0表示False，用数字1表示True

2. String （字符串）   
    字符串属于序列类型，Python将字符串视为一连串的字符组合

3. List （列表）

4. Tuple （元组）

5. Sets （集合）

6. Dictionary （字典）
<br>

# 运算符和优先级
1. 算数运算符

2. 比较运算符

3. 赋值运算符

4. 逻辑运算符 and / or /  not

5. 位运算符

6. 成员运算符 in / not in

7. 身份运算符 is / not is
<br>

# 列表的基本操作
列表（list）对象属于序数对象，它是一群有序对象的集合，并且可以使用数字来做索引。  
```python
list.index()
list.insert(index,value)
del list[index]
```

## 列表包容 
从Python2.0开始，可以使用列表包容（list comprehension）功能。所谓列表包容是使用列表内的元素，来创建新的列表。  

## 列表常用的操作符：+ *
\+ ： 用于列表的组合，用在两个列表中  
\* ： 用于重复列表，一个列表，一个整数  
<br>

输入dir([])就可以显示内置方法

---
len()  
max()  列表中元素数据类型必须一致  
min()  列表中元素数据类型必须一致  
list()  
sum() 列表中元素必须是数字  

---

append()  
clear()  
copy()  
count(value) 将列表对象中的元素值为value者，计算其数目  
extend()
index(value)
pop([index]) : 参数可选，没有填入index，则删除列表中的最后一个元素  
remove(value) : value不在列表中会报错  
reverse() : 颠倒  
sort() : 列表中的元素必须是同一类型