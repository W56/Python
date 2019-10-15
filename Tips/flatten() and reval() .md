# np.flatten() and np.reval()

相同点：功能是将多维数组降成一维  

区别：返回的是拷贝还是视图，numpy.flatten()返回一份拷贝，对拷贝所做的修改不会影响原始矩阵，而numpy.reval()返回的是视图（view）,会影响原始矩阵

## 二者的功能

```python
>>> import numpy as np
>>> x = np.array([[1,2],[3,4]])
>>> x
array([[1, 2],
       [3, 4]])
>>> x.flatten()
array([1, 2, 3, 4]) # 默认是行序优先
>>> x.ravel()
array([1, 2, 3, 4])
>>> x.flatten('F')
array([1, 3, 2, 4])
>>> x.ravel('F')
array([1, 3, 2, 4])
>>> x
array([[1, 2],
       [3, 4]])
>>> x.reshape(-1)
array([1, 2, 3, 4])
>>> x.T.reshape(-1)
array([1, 3, 2, 4])
```

## 两者的区别

```python
>>> x = np.array([[1,2],[3,4]])
>>> x.flatten()[1] = 100
>>> x
array([[1, 2],
       [3, 4]])
>>> x.ravel()[1] = 100
>>> x
array([[  1, 100],
       [  3,   4]])
```