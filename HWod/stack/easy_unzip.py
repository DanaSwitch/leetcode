"""
思路: 遇到左括号入栈, cur = "", 遇到右括号出栈,stack.pop(), 拼接
"""
import sys

def solve():
    s = sys.stdin.readline().strip()
    if not s:
        return
    
    stack = []  # 保存上一层的字符串
    cur = [] # 用列表存储字符串片段，最后统一 join
    i = 0
    
    while i < len(s):
        if s[i].isalpha():
            char = s[i]
            # 获取紧跟的数字
            i += 1
            num_str = ""
            while i < len(s) and s[i].isdigit():
                num_str += s[i]
                i += 1  # 可能多位数字
            num = int(num_str)
            cur.append(char * num)  # 复制num位
            
        elif s[i] == '{':
            # 进入嵌套：将当前层压栈进行保存
            stack.append(cur)
            cur = []
            i += 1
            
        elif s[i] == '}':
            # 获取括号后的数字
            i += 1
            num_str = ""
            while i < len(s) and s[i].isdigit():
                num_str += s[i]
                i += 1
            num = int(num_str)
            
            combined_str = "".join(cur)  # 将当前层的结果合并
            cur = stack.pop()
            cur.append(combined_str * num)  # 乘以重复次数
            
    print("".join(cur))

if __name__ == "__main__":
    solve()