import sys
import re

def calc(a, b, op):
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
    
    nums = []
    ops = []
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
        elif s[i] == ')':
            while ops[-1] != '(':
                b = nums.pop(); a = nums.pop()
                nums.append(calc(a, b, ops.pop()))
            ops.pop()
        else:
            while ops and ops[-1] != '(' and priority[ops[-1]] >= priority[s[i]]:
                b = nums.pop(); a = nums.pop()
                nums.append(calc(a, b, ops.pop()))
            ops.append(s[i])
        i += 1
    
    while ops:
        b = nums.pop(); a = nums.pop()
        nums.append(calc(a, b, ops.pop()))
    
    print(nums[0])

solve()