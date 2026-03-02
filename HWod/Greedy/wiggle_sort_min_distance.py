import sys

def main():
    line = sys.stdin.readline().strip()
    if not line:
        return # 或者根据题目要求输出 []

    parts = line.split()
    ans = []
    
    # 1. 严格校验输入
    for s in parts:
        if not s.isdigit():
            print("[]") # 严格匹配示例 3 的输出
            return
        ans.append(int(s))
    
    # 2. 修正后的贪心算法
    # 规则：i 为偶数时 ans[i] >= ans[i+1] (高)；i 为奇数时 ans[i] <= ans[i+1] (矮)
    for i in range(len(ans) - 1):
        if i % 2 == 0:
            if ans[i] < ans[i+1]:
                ans[i], ans[i+1] = ans[i+1], ans[i]
        else:
            if ans[i] > ans[i+1]:
                ans[i], ans[i+1] = ans[i+1], ans[i]

    print(" ".join(map(str, ans)))

if __name__ == "__main__":
    main()