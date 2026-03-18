import sys
import re
from fractions import Fraction

# 定义运算符优先级
priority = {'+': 1, '-': 1, '*': 2, '/': 2}

def compute(ops, nums):
    if len(nums) < 2: return
    op = ops.pop()
    b = nums.pop()
    a = nums.pop()
    if op == '+': nums.append(a + b)
    elif op == '-': nums.append(a - b)
    elif op == '*': nums.append(a * b)
    elif op == '/':
        if b == 0: raise ZeroDivisionError # 还是抛出异常，方便统一处理
        nums.append(a / b)

def solve():
    # 预处理：去掉空格，处理负号（本题说没有负数，但为了稳健可以保留）
    s = sys.stdin.read().replace(' ', '').replace('-(', '-1*(')
    if not s: return

    # 提取数字和符号
    tokens = re.findall(r'\d+|[\+\-\*\/\(\)]', s)
    
    nums = [] # 数字栈
    ops = []  # 符号栈

    try:
        i = 0
        while i < len(tokens):
            t = tokens[i]
            if t.isdigit():
                nums.append(Fraction(int(t)))
            elif t == '(':
                ops.append(t)
            elif t == ')':
                while ops and ops[-1] != '(':
                    compute(ops, nums)
                ops.pop() # 弹出 '('
            else:
                # 遇到运算符，比较优先级
                while ops and ops[-1] != '(' and priority[ops[-1]] >= priority[t]:
                    compute(ops, nums)
                ops.append(t)
            i += 1
        
        while ops:
            compute(ops, nums)
            
        res = nums[0]
        if res.denominator == 1:
            print(res.numerator)
        else:
            print(f"{res.numerator}/{res.denominator}")
            
    except ZeroDivisionError:
        print("ERROR")

solve()