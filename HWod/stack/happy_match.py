def solution(s):
    # 1. 异常输入检查：如果不全是字母，返回 0
    if not s.isalpha():
        return 0
    
    stack = []
    
    for char in s:
        # 2. 如果栈不为空且栈顶元素等于当前字符，进行消除
        if stack and stack[-1] == char:
            stack.pop()
        else:
            # 3. 否则，将字符入栈
            stack.append(char)
            
    # 4. 返回栈中剩余元素的长度
    return len(stack)

# 测试代码
print(solution("gg"))      # 输出: 0
print(solution("adbbdc"))  # 输出: 2