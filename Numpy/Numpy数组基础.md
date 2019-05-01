# Numpy 
## 1.从Python列表创建数组
np.array()
## 2.从头创建数组
1.np.zeros()<br>
2.np.ones()<br>
3.np.full((3,5),3.14) 创建一个3x5的浮点类型数组，数组的值都是3.14<br>
4.np.arrange(0,20,2) 创建一个线性序列数组，从0开始，到20结束，步长为2<br>
5.np.linespace(0,1,5) 这5个数均匀的分配0-1<br>
6.np.random.random((3,3)) 创建1个3x3的、在0-1均匀分布的随机数组成的数组<br>
7.np.random.normal(0,1,(3,3)) 正态分布的随机数组<br>
8.np.random.randint(0,10,(3,3)) 创建一个3x3的、\[0,10\)区间的随机整数<br>
9.np.eye(3) 创建1个3x3的单位矩阵<br>
10.np.empty(3) 创建1个由3个整数组成的未初始化的数组<br>
## 3.NumPy标准数据类型 <br>
当构建一个数组时，可以使用一个字符串参数来指定数据类型<br>
```python
np.zeros(10,dtype='int16)
```
名称 | 描述 
-|- 
bool_ | 布尔型数据类型（True 或者 False）
int_	| 默认的整数类型（类似于 C 语言中的 long，int32 或 int64）
intc	| 与 C 的 int 类型一样，一般是 int32 或 int 64
intp	| 用于索引的整数类型（类似于 C 的 ssize_t，一般情况下仍然是 int32 或 int64）
int8	| 字节（-128 to 127）
int16	| 整数（-32768 to 32767）
int32	| 整数（-2147483648 to 2147483647）
int64	| 整数（-9223372036854775808 to 9223372036854775807）
uint8	| 无符号整数（0 to 255）
uint16	| 无符号整数（0 to 65535）
uint32	| 无符号整数（0 to 4294967295）
uint64	| 无符号整数（0 to 18446744073709551615）
float_	| float64 类型的简写
float16	| 半精度浮点数，包括：1 个符号位，5 个指数位，10 个尾数位
float32	| 单精度浮点数，包括：1 个符号位，8 个指数位，23 个尾数位
float64	| 双精度浮点数，包括：1 个符号位，11 个指数位，52 个尾数位
complex_	| complex128 类型的简写，即 128 位复数
complex64	| 复数，表示双 32 位浮点数（实数部分和虚数部分）
complex128	| 复数，表示双 64 位浮点数（实数部分和虚数部分）

## 4.NumPy数组的属性
确定数组的大小，形状，存储大小，数据类型<br>
1.  每个数组有ndim（数组的维度），shape（数组每个维度的大小）和size（数组的总大小）<br>
```python
import numpy as np
np.random.seed(0) #设置随机种子
x1 = np.random.randint(10,size=6) #一维数组
x2 = np.random.randint(10,size=(3,4)) #二维数组
x3 = np.random.randint(10,size=(3,4,5)) #三维数组
print(x3.ndim) #3
print(x3.shape) #(3,4,5)
print(x3.size) #60
```
2. 另外一个有用的属性是dtype，它是数组的数据类型
```python
print(x3.dtype) #int32
```
## 5.数组索引：获取单个元素
1.在一维数组中，通过中括号索引第i个值<br>
2.为了获取数组末尾的值，可以用负数索引<br>
3.在多维数组中，可以用逗号分隔获取具体元素，也可以用多个中括号<br>
```python
print(x[0,0])
print(x[0][0])
```
## 6.数组切片：获取子数组
NumPy切片语法和Python列表的标准切片语法相同<br>
多维也可以采用同样的方式处理，用“，”分隔<br>
```python
x[start:stop:step]
```
1.非副本视图的子数组
数组切片返回的是数组数据的**视图**，而不是数值数据的**副本**，在Python列表切片中，切片是值的副本<br>
它意味着在处理非常大的数据集时，可以获取或处理这些数据的片段，而不用复制底层的数据缓存。<br>
```python
x = [0,1,2,3,4,5,6]
y = x[0:4]
y[0] = 1
print(x) #[0, 1, 2, 3, 4, 5, 6]
print(y) #[1, 1, 2, 3]
```
2.创建数组的副本 copy方法实现
## 7.数组的变形
reshape()方法将会用到一个原始数组的**非副本视图**
## 8.数组的拼接和分裂
拼接或连接Numpy中的两个数组主要由np.concatenate、np.vstack和np.hstack<br>
1.数组的拼接<br>
 - 1.concatenate可以用于一维数组，二维数组的连接<br>
```python
x = np.array([1,2,3])
y = np.array([3,2,1])
z = [99,99,99]
np.concatenate([x,y]) 
# array([1, 2, 3, 3, 2, 1])

np.concatenate([x,y,z]) 
#array([ 1,  2,  3,  3,  2,  1, 99, 99, 99])

grid = np.array([[1,2,3],[4,5,6]])
np.concatenate([grid,grid]) 
#沿着第一个轴拼接
#array([[1, 2, 3],
#      [4, 5, 6],
#      [1, 2, 3],
#      [4, 5, 6]])

np.concatenate([grid,grid],axis=1)
#沿第二个轴拼接
#array([[1, 2, 3, 1, 2, 3],
#       [4, 5, 6, 4, 5, 6]])
```
- 2.沿着固定维度处理数组时，使用np.vstack (垂直栈)和np.hstack (水平栈)函数会更简洁
```python
x = np.array([1,2,3])
grid = np.array([[9,8,6],[3,4,5]])
np.vstack([x,grid])
#array([[1, 2, 3],
#      [9, 8, 6],
#      [3, 4, 5]])

y = np.array([[99],[99]])
np.hstack([grid,y])
#array([[ 9,  8,  6, 99],
#       [ 3,  4,  5, 99]])
```
2.数组的分裂<br>
与拼接过程相反，通过np.split，np.hsplit，np.vsplit<br>
```python
x = [1,2,3,99,99,3,2,1]
x1,x2,x3 = np.split(x,[3,5]) #索引列表记录的是分裂点的位置
print(x1,x2,x3) #[1 2 3] [99 99] [3 2 1]
grid = np.arange(16).reshape((4,4))
#array([[ 0,  1,  2,  3],
#       [ 4,  5,  6,  7],
#       [ 8,  9, 10, 11],
#       [12, 13, 14, 15]])

upper,lower = np.vsplit(grid,[2])
print(upper)
#[[0 1 2 3]
#[4 5 6 7]]

print(lower)
#[[ 8  9 10 11]
# [12 13 14 15]]

left,right = np.hsplit(grid,[2])
print(left)
#[[ 0  1]
# [ 4  5]
# [ 8  9]
# [12 13]]

print(right)
#[[ 2  3]
# [ 6  7]
# [10 11]
# [14 15]]
```
