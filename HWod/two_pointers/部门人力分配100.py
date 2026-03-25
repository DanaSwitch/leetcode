"""
题目描述
小明是一个项目经理，最近他接了一个大项目，需要在 M 个月内完成 N 个需求。
每个需求都有一个开发时间要求，单位是月。
小明想知道，最少需要多少人手才能在 M 个月内完成所有需求。
要求: 1<=N/2<=M<=N
M是开发时间要求, N是需求数量
分析:
N<=2M, 说明每个月至少要干一个活，最多可以干两个活。
"""
import sys


def solve():
    input_data = sys.stdin.read().split()
    literator = iter(input_data)
    M = int(next(literator))
    requirments = [int(x) for x in literator]
    N = len(requirments)
    # 排序
    requirments.sort()

    def check(limit):
        l, r = 0, N-1
        month = 0
        while l <= r:
            if l < r and requirments[l] + requirments[r] <= limit:
                l += 1    
            month += 1
            r -= 1
        return month <= M

    # 二分法找到满足条件的最小的数
    left = requirments[-1]  # 最小的值
    if N>1:
        right = requirments[-1] + requirments[-2]
    else:
        right = requirments[-1]

    while left < right:
        mid = (left + right) // 2
        if check(mid):
            right = mid
        else: # mid不够用, 增大mid
            left = mid + 1 
    print(left)

if __name__ == "__main__":
    solve()