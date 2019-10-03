import matplotlib.pyplot as plt
from pylab import mpl
import math
import numpy as np
import pandas as pd

def get_difference_quotient(X,Y):
    '''
    获取差商表
    '''
    n = len(X)
    A = np.zeros((n,n))

    for i in range(n):
        A[i][0] = Y[i]
    for j in range(1,n):
        for i in range(j,n):
            A[i][j] = (A[i][j-1]-A[i-1][j-1])/(X[i]-X[i-j])

    return A

def newton_interpolation(X,Y,x):
    '''
    计算x点的插值
    '''
    global A
    sum = Y[0]
    temp_sum = 1.0
    for j in range(1,len(X)):
        # x的多项式
        temp_sum *= (x-X[j-1])
        # 计算均差
        sum += (A[j][j]*temp_sum)
    return sum

X=[-1,0,1,2,3,4,5]
Y=[-20,-12,1,15,4,21,41]

# 画图
data_x=np.linspace(np.min(X),np.max(X),1000,endpoint=True)
data_y=[]
A = get_difference_quotient(X,Y)
for x in data_x:
    data_y.append(newton_interpolation(X,Y,x))

plt.title("newton_interpolation")
plt.plot(X,Y,'s',label="original values")#蓝点表示原来的值
plt.plot(data_x,data_y,'r',label='interpolation values')#插值曲线
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc="upper left")#指定legend的位置右下角
plt.show()

print(A)