"""
思路: 核心是 min_cur 和 max_cur 的处理, 然后第一个人分配的月饼数也要穷举
"""
import sys

def solve(m, n):
    memo = {}

    def dp(emp_left, moon_left, prev):  # 还需要分给多少个员工, 剩余月饼数, 上一个人分了多少月饼 
        if emp_left == 0:
            # 剩余月饼数为0说明刚好分完, 属于一种方案
            return 1 if moon_left == 0 else 0

        key = (emp_left, moon_left, prev)
        if key in memo:
            return memo[key]

        min_cur = max(1, prev - 3)  # 最少分1, 且比前一人不低于3个
        max_cur = min(prev, moon_left - (emp_left - 1))  # 最多不超过前一个, 且后序每人至少一个
        # 不能按要分配
        if min_cur > max_cur:
            memo[key] = 0
            return 0

        result = 0
        for cur in range(min_cur, max_cur + 1):
            result += dp(emp_left - 1, moon_left - cur, cur)
        # 记录
        memo[key] = result
        return result

    total = 0
    max_first = n - (m - 1)
    # 穷举: 假设第一个人拿了1, 2, 3, ..., n-(m-1)个
    for first in range(1, max_first + 1):
        total += dp(m - 1, n - first, first)

    return total

m, n = map(int, input().strip().split())
print(solve(m, n))