"""
思路: 正序: 先定义好初始状态, 从10出发, 看最后A是M的组合数
"""

def solve(m):
    a = [0] * (m+1)  # a[i] 表示上一轮b是i, b赢的方案数
    b = [0] * (m+1)  # bi] 表示上一轮a是i, b赢的方案数

    a[8], a[9] =0, 1
    b[8], b[9] =1, 1  
    for i in range(10, m+1):
        a[i] = b[i-1] + b[i-2]
        b[i] = a[i-1] + a[i-2]
    print(b[m])

if __name__ == "__main__":
    m = int(input())
    solve(m)