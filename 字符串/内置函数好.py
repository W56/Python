#实际开发时，优先考虑使用python的内置函数和内置对象的方法，运行速度快，并且运行稳定。
from string import ascii_letters
from random import choice
from time import time

letters = ' '.join([choice(ascii_letters)for i in range (999999)])
def positions_of_character(setence,ch):
    result = []
    index = 0
    index = setence.find(ch,index+1)
    while index!=-1:
        result.append(index)
        index = setence.find(ch,index+1)
    return result

def demo(s,c):
    result = []
    for i,ch in enumerate(s):
        if ch==c:
            result.append(i)
    return result

start = time()
positions = positions_of_character(letters,'a')
print(time()-start)

start = time()
p = demo(letters,'a')
print(time()-start)

#在jupyter notebook中的运行结果
#0.01496577262878418
#0.2537190914154053
