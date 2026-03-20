"""
第三题是实现计算器，有加减乘平方和平方差和平方积，平方积优先度最高，下来平方和和平方差，然后输入一个字符串，
可能一个式子有多个括号就是( (11+25) )这种, 字符串可能有空格但是一个数11之间不能有空格,
除了运算符只有0-9, 运算数字有两位数, 求最后结果
"""
import sys
import re

def opearate(a, b, op):
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '@': return (a * b) ** 2      # 平方积
    if op == '$': return a*a + b*b         # 平方和
    if op == '#': return a*a - b*b         # 平方差

def solve():
    s = sys.stdin.readline().rstrip()
    
    # 检测数字之间有空格（含多个空格）
    if re.search(r'\d\s+\d', s):
        print(-1)
        return
    
    s = s.replace(" ", "")
    
    # 修复：* 优先级高于 +/-
    priority = {'@': 4, '$': 3, '#': 3, '*': 2, '+': 1, '-': 1}
    
    nums = []  # 运算数
    ops = []  # 操作符
    i = 0
    while i < len(s):
        if s[i].isdigit():
            num = 0
            while i < len(s) and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            nums.append(num)
            continue
        elif s[i] == '(':
            ops.append(s[i])
        elif s[i] == ')':  # 弹出
            while ops[-1] != '(':
                b = nums.pop()
                a = nums.pop()
                nums.append(opearate(a, b, ops.pop()))
            ops.pop()  # 弹出)
        else:
            while ops and ops[-1] != '(' and priority[ops[-1]] >= priority[s[i]]:
                b = nums.pop()
                a = nums.pop()
                nums.append(opearate(a, b, ops.pop()))
            ops.append(s[i])
        i += 1
    
    while ops:
        b = nums.pop()
        a = nums.pop()
        nums.append(opearate(a, b, ops.pop()))
    
    print(nums[0])

solve()