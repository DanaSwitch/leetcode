import sys

x, y, cntx, cnty = map(int, input().split())
"""
map(函数, 可迭代对象) map将可迭代对象的每个元素以此应用到函数上, 并返回一个包含结果的新可迭代对象
input().spilt() 对输入字符串进行分割
"""

def check(num):
    # 1-num中x的倍数的数量
    xCount = num // x
    # 1-num中y的倍数的数量
    yCount = num // y
    # 1-num中x*y的倍数的数量
    xyCount = num // (x * y)
    
    # 只能去x国的人数
    only_x = yCount - xyCount
    # 只能去y国的人数
    only_y = xCount - xyCount
    # 两国都能去的人数
    both = num - xCount - yCount + xyCount
    
    # x国还需要的人数
    need_x = cntx - only_x if cntx > only_x else 0
    # y国还需要的人数
    need_y = cnty - only_y if cnty > only_y else 0
    
    return need_x + need_y <= both

if __name__ == "__main__":
    # 使用倍增+二分
    # 先倍增找到上界
    hi = 1
    while not check(hi):
        hi <<= 1
    
    # 二分查找最小k
    lo = 1
    while lo < hi:
        mid = (lo + hi) // 2
        if check(mid):
            hi = mid
        else:
            lo = mid + 1
    
    print(lo)