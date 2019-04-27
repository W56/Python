
import random

def quick_sort(x,start,end):

    # 如果start和end碰头了，说明要我排的这个子数列就剩下一个数了，就不用排序了
    if start >= end:
        return

    #拿出第一个数当作基准mid
    mid = x[start]
    #low来标记左侧从基准数始找比mid大的数的位置
    low = start
    #high来标记右侧从基准数始找比mid小的数的位置
    high = end

    #我们要进行循环，只要low和high没有碰头就一直进行,当low和high相等说明碰头了
    while low < high:

        #从high开始向左，找到第一个比mid小或者等于mid的数，标记位置,（如果high的数比mid大，我们就左移high）
        #并且我们要确定找到之前，如果low和high碰头了，也不找了
        while low<high and mid <= x[high]:
            high -= 1
        #跳出while后，high所在的下标就是找到的右侧比mid小的数
        #把找到的数放到左侧的空位 low 标记了这个空位
        x[low] = x[high]

        while low<high and mid >= x[low]:
            low += 1
        x[high] = x[low]
    #当这个while跳出来之后相当于low和high碰头了，我们把mid所在位置放在这个空位
    x[low] = mid
    #这个时候mid左侧看的数都比mid小，mid右侧的数都比mid大

    #然后我们对mid左侧以及右侧所有数进行上述的排序
    quick_sort(x,start,high-1)
    quick_sort(x,high+1,end)


if __name__ == '__main__':
    x = list(range(1, 10))
    random.shuffle(x)
    print(x)
    length = len(x) - 1
    quick_sort(x, 0, length)
    print(x)

