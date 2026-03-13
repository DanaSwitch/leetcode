"""
思路: 双队列, 分段比较
"""
from collections import deque
import sys

def parse(s):
    res, num = deque(), ""
    for c in s:
        if c.isdigit():  # 判断数字
            num += c
        else:
            res.append((c, int(num) if num else 1))  # 前面没数字, 但有字母则输入1
            num = ""
    return res

s1 = sys.stdin.readline().strip()
s2 = sys.stdin.readline().strip()

q1, q2 = parse(s1), parse(s2)  # 标准字符串, 传输后字符串
errors, total = 0, 0  # 错误数, 解压后长度

while q1:
    c1, n1 = q1.popleft()
    c2, n2 = q2.popleft()
    compare = min(n1, n2)

    if c1 != c2:
        errors += compare
    total += compare
    # 将多的压回队列
    if n1 > compare: q1.appendleft((c1, n1 - compare))
    if n2 > compare: q2.appendleft((c2, n2 - compare))

print(f"{errors}/{total}")