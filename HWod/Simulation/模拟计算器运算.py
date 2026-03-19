def solve_calculator():
    # 1. 直接读取输入并去除所有空格
    s = input().strip().replace(" ", "")
    if not s:
        return

    # 2. 定义运算符优先级（考试时请换成题目实际的符号）
    precedence = {
        '+': 1, 
        '-': 1,
        '*': 2,
        '#': 3,  # 平方和
        '@': 3,  # 平方差
        '$': 4   # 平方积
    }

    nums = [] # 操作数栈
    ops = []  # 运算符栈

    # 计算出栈的函数
    def calculate():
        if len(nums) < 2 or not ops:
            return
        b = nums.pop() # 注意：先出栈的是右侧的数字
        a = nums.pop()
        op = ops.pop()
        
        if op == '+': nums.append(a + b)
        elif op == '-': nums.append(a - b)
        elif op == '*': nums.append(a * b)
        elif op == '#': nums.append(a**2 + b**2)
        elif op == '@': nums.append(a**2 - b**2)
        elif op == '$': nums.append((a**2) * (b**2))

    i = 0
    n = len(s)
    is_unary = True # 用于判断减号是否代表负数

    while i < n:
        c = s[i]
        
        # 处理数字（包括多位数）
        if c.isdigit():
            num = 0
            while i < n and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            nums.append(num)
            is_unary = False
            continue # 因为这里的i已经指向下一个非数字字符了，所以直接continue
            
        # 处理左括号
        elif c == '(':
            ops.append(c)
            is_unary = True
            
        # 处理右括号
        elif c == ')':
            while ops and ops[-1] != '(':
                calculate()
            if ops:
                ops.pop() # 弹出左括号 '('
            is_unary = False
            
        # 处理运算符
        elif c in precedence:
            # 兼容负数：如果减号前面没有数字或刚遇过左括号，补0变为 0-x
            if c == '-' and is_unary:
                nums.append(0)
            else:
                # 优先级判断：栈顶优先级 >= 当前运算符，就一直计算
                while ops and ops[-1] != '(' and precedence[ops[-1]] >= precedence[c]:
                    calculate()
            ops.append(c)
            is_unary = True
            
        i += 1

    # 遍历完字符串后，把栈里剩下的算完
    while ops:
        calculate()

    # 栈底剩下的唯一数字就是最终答案
    print(nums[0] if nums else 0)

if __name__ == "__main__":
    solve_calculator()