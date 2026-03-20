"""
(div 1 0) 输出: error
除法遇除不尽，向下取整，即 3/2 = 1, (-7)/3 = -3
输入描述:
输入为长度不超过512的字符串, 用例保证了无语法错误
输出描述:
输出计算结果或者“error”

输入: (add 1 (div -7 3))
输出: -2
说明: -7除以3向下取整得-3, 1加-3得-2
"""
s = input()

def operate(op, p1, p2):
    p1, p2 = int(p1), int(p2)
    if op == "add":
        return p1 + p2
    elif op == "sub":
        return p1 - p2
    elif op == "mul":
        return p1 * p2
    elif op == "div":
        if p2 == 0:
            return "error"
        return p1 // p2

def solve():
    # 分词
    # 原始括号和词之间没有空格, 给它们加上空格
    tokens = s.replace('(', ' ( ').replace(')', ' ) ').split()
    # → ['(', 'add', '1', '(', 'div', '6', '3', ')', ')']

    stack = []

    for token in tokens:
        if token == ')':
            # 弹出直到遇到 (
            p2 = stack.pop()  # 注意先弹出p2
            p1 = stack.pop()
            op = stack.pop()
            stack.pop()  # 弹出 (

            if p1 == "error" or p2 == "error":
                stack.append("error")
            else:
                res = operate(op, p1, p2)
                # 统一str类型一致, 不用判断每次运算前要 int() 转换
                stack.append(str(res))
        else:
            stack.append(token)  # ( 、op、数字 直接压栈

    return stack[0]

print(solve())