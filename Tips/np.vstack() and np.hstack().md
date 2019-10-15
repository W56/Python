# np.vstack() and np.hstack()

np.vstack() : 在竖直方向上堆叠  

np.hstack() : 在水平方向上平铺

```python
>>> import numpy as np
>>> arr1 = np.array([1,2,3])
>>> arr2 = np.array([4,5,6])
>>> np.vstack((arr1,arr2))
array([[1, 2, 3],
       [4, 5, 6]])
>>> np.hstack((arr1,arr2))
array([1, 2, 3, 4, 5, 6])
```

## hstack

## 第一例
```python
>>> brr1 = np.array([1,2,3,4,5,6,7,8,9,10,11])
>>> brr1_folds = np.array_split(brr1,3)
>>> brr1_folds
[array([1, 2, 3, 4]), array([5, 6, 7, 8]), array([ 9, 10, 11])]
>>> brr1_folds[0:2]+brr1_folds[1:3]
[array([1, 2, 3, 4]), array([5, 6, 7, 8]), array([5, 6, 7, 8]), array([ 9, 10, 11])]
>>> np.hstack((brr1_folds[:2]+brr1_folds[1:3]))
array([ 1,  2,  3,  4,  5,  6,  7,  8,  5,  6,  7,  8,  9, 10, 11])
>>> brr1_folds[0:2]
[array([1, 2, 3, 4]), array([5, 6, 7, 8])]
>>> brr1_folds[1:3]
[array([5, 6, 7, 8]), array([ 9, 10, 11])]
#print np.hstack((brr1_folds[0:2],brr1_folds[1:3])) 注意中间是加号连接，因为维度不一致
>>> np.hstack((brr1_folds[0:2],brr1_folds[1:3]))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "D:\Anaconda\envs\py36\lib\site-packages\numpy\core\shape_base.py", line 340, in hstack
    return _nx.concatenate(arrs, 1)
ValueError: all the input arrays must have same number of dimensions
#错误的原因就是以为我的array的维度不一致。改成+就好啦，加号是list的拼接！
```


## 第二例
结果是：表明了一维的数组hstack是随意的。
```python
>>> print( np.hstack(([1,2,3,3,4],[3,4,5,8,6,6,7])))
[1 2 3 3 4 3 4 5 8 6 6 7]
```

## 第三例
表明我们的hstack必须要第二维度是一样的
```python
>>> np.hstack(([1,2,3,3,4],[3,4,5,8,6,6,7]))
array([1, 2, 3, 3, 4, 3, 4, 5, 8, 6, 6, 7])
>>> np.hstack(([[1,2,3],[2,3,4]],[[1,2],[2,3]]))
array([[1, 2, 3, 1, 2],
       [2, 3, 4, 2, 3]])
>>> np.hstack(([[1,2,3],[2,3,4]],[[1,2]]))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "D:\Anaconda\envs\py36\lib\site-packages\numpy\core\shape_base.py", line 340, in hstack
    return _nx.concatenate(arrs, 1)
ValueError: all the input array dimensions except for the concatenation axis must match exactly
```

## vstack

## 第一例

```python
>>> np.vstack(([1,2,3],[3,4,3]))
array([[1, 2, 3],
       [3, 4, 3]])
>>> np.vstack(([1,2,3],[2,3]))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "D:\Anaconda\envs\py36\lib\site-packages\numpy\core\shape_base.py", line 283, in vstack
    return _nx.concatenate([atleast_2d(_m) for _m in tup], 0)
ValueError: all the input array dimensions except for the concatenation axis must match exactly
```

## 第二例

```python
>>> np.vstack(([[1,2,3],[3,4,3]],[[1,3,4],[2,4,5]]))
array([[1, 2, 3],
       [3, 4, 3],
       [1, 3, 4],
       [2, 4, 5]])
>>> np.vstack(([[1,2,3],[3,4,3]],[[3,4],[4,5]]))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "D:\Anaconda\envs\py36\lib\site-packages\numpy\core\shape_base.py", line 283, in vstack
    return _nx.concatenate([atleast_2d(_m) for _m in tup], 0)
ValueError: all the input array dimensions except for the concatenation axis must match exactly
```