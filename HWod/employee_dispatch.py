"""
2025_1204 双机位C卷 员工派遣
某公司部门需要派遣员工去国外做项目.
现在, 代号为 x 的国家和代号为 y 的国家分别需要 cntx 名和 cnty 名员工.
部门每个员工有一个员工号(1,2,3,......), 工号连续, 从1开始.

部长派遣员工的规则:
规则1: 从 [1, k] 中选择员工派遣出去
规则2: 编号为 x 的倍数的员工不能去 x 国, 编号为 y 的倍数的员工不能去 y 国.

问题: 找到最小的 k, 使得可以将编号在 [1, k] 中的员工分配给 x 国和 y 国,
且满足 x 国和 y 国的需求.

输入描述:
四个整数 x, y, cntx, cnty.
约束条件:

2 ≤ x < y ≤ 30000
x 和 y 一定是质数
1 ≤ cntx, cnty < 10^9
cntx + cnty ≤ 10^9
输出描述:
满足条件的最小的k
------
解题思路:
数论分类: 根据整除性质将员工分为四类
只能去x国: 是y的倍数但不是x的倍数
只能去y国: 是x的倍数但不是y的倍数
两国都不能去: 同时是x和y的倍数
两国都能去: 既不是x的倍数也不是y的倍数
贪心分配: 先给x国和y国分配只能去x国和只能去y国的员工,然后再计算x国和y国需要的人数,
再从剩下x和y国都能去的员工中挑选,need_x + need_y <= both ,就返回false
二分查找: 利用单调性(k越大越容易满足需求)二分搜索最小k值
"""

import sys
#x,y为代码为x,y的国家, cntx为x国需要的人数, cnty为y国所需要的人数
x, y, cntx, cnty = map(int, input().split())
"""
map(函数, 可迭代对象) map将可迭代对象的每个元素以此应用到函数上, 并返回一个包含结果的新可迭代对象
input().spilt() 对输入字符串进行分割
"""

def check(num):
    # 1-num中x的倍数的数量，去x国的员工数量
    xCount = num // x
    # 1-num中y的倍数的数量，去y国的员工数量
    yCount = num // y
    # 1-num中x*y的倍数的数量, x国和y国都能去的员工数量
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
    high = 1
    while not check(high):
        high <<= 1
    
    # 二分查找最小k
    low = 1
    while low < high:
        mid = (low + high) // 2
        if check(mid):
            high = mid
        else:
            low = mid + 1
    
    print(low)