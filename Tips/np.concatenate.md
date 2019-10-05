# np.concatenate 
concatenate((a1,a2,...),axis=0)  

数组拼接函数  

参数：  

a1，a2，...，为要拼接的数组  
axis：要在哪个维度上进行拼接，默认值为0  

```python
>>> import numpy as np
>>> a = np.array([1,2,3])
>>> b = np.array([11,22,33])
>>> c = np.array([44,55,66])
>>> np.concatenate((a,b,c),axis=0)
array([ 1,  2,  3, 11, 22, 33, 44, 55, 66])
#对于一维数组拼接，axis的值不影响最后的结果

>>> a = np.array([[1,2,3],[4,5,6]])
>>> b = np.array([[11,21,31],[7,8,9]])
>>> np.concatenate((a,b),axis=0)
array([[ 1,  2,  3],
       [ 4,  5,  6],
       [11, 21, 31],
       [ 7,  8,  9]])
#axis=1表示对应行的数组进行拼接
>>> np.concatenate((a,b),axis=1)
array([[ 1,  2,  3, 11, 21, 31],
       [ 4,  5,  6,  7,  8,  9]])
>>> a = np.array([[1,2],[3,4]])
>>> b = np.array([[5,6]])
>>> np.concatenate((a,b),axis=0)
array([[1, 2],
       [3, 4],
       [5, 6]])
>>> np.concatenate((a,b.T),axis=1)
array([[1, 2, 5],
       [3, 4, 6]])
```