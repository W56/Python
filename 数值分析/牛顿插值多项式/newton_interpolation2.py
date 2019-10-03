import matplotlib.pylab as plt
import numpy as np
import pandas as pd



'''
fun1 采用的是k阶均差的性质来求解k阶均差的值
fun2 采用的是算出均差表的形式来求解
'''

def fun1(X,Y):
    if len(X) < 2:
        print("X\'s length must be bigger than 2")
        return
    ans = 0
    for i in range(len(X)):
        temp = 1
        for j in range(len(X)):
            if i==j:
                continue
            else:
                temp *= (X[i]-X[j])
        ans += Y[i]/temp
    return ans

def fun2(X,Y):
    n = len(X)
    A = np.zeros((n,n))

    for i in range(n):
        A[i][0] = Y[i]
    for j in range(1,n):
        for i in range(j,n):
            A[i][j] = (A[i][j-1]-A[i-1][j-1])/(X[i]-X[i-j])
    quotient = []
    for i in range(n):
        quotient.append(A[i][i])
    return quotient


def newton_interpolation(X,Y,x):
    global quotient1
    global quotient2
    sum1 = Y[0]
    sum2 = Y[0]
    temp_sum = 1.0
    for j in range(1,len(X)):
        # x的多项式
        temp_sum *= (x-X[j-1])
        # 计算均差
        sum1 += (quotient1[j]*temp_sum)
        sum2 += (quotient2[j] * temp_sum)
    return sum1,sum2

X = [0.4,0.55,0.65,0.80,0.90,1.05]
Y = [0.41075,0.57815,0.69675,0.88811,1.02652,1.25382]
quotient1 = [0.41075]
data_x = [0.4,0.55]
data_y = [0.41075,0.57815]


i = 1
while len(data_x) < len(X):
    quotient1.append(fun1(data_x,data_y))
    i += 1
    data_x.append(X[i])
    data_y.append(Y[i])

quotient1.append(fun1(X,Y))
# print(quotient1)
#[0.41075, 1.116, 0.28000000000000114, 0.1973333333333258, 0.03123809523822274, 0.0002930402926608622]


quotient2 = fun2(X,Y)
# print(quotient2)
# [0.41075, 1.116, 0.2799999999999976, 0.19733333333334047, 0.03123809523812543, 0.0002930402927728068]

x = np.linspace(np.min(X),np.max(X),1000,endpoint=True)
y1 = []
y2 = []

for i in x:
    y1.append(newton_interpolation(X,Y,i)[0])
    y2.append(newton_interpolation(X,Y,i)[1])

# 可以看出两条线基本重合

plt.title("newton_interpolation")
plt.plot(X,Y,'s',label="original values")#蓝点表示原来的值
# plt.plot(x,y1,'r',label='interpolation values')#插值曲线,系数是quotient1
plt.plot(x,y2,'g',label='interpolation values')#插值曲线,系数是quotient2
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc="upper left")#指定legend的位置右下角
plt.show()