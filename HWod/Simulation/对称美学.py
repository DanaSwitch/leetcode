import sys

def solve(n, k):
    if n == 1:
        return 0
    if n == 2:
        return 1 if k == 0 else 0

    half = 1 << (n - 2)
    # 后半部分和上一行的 k -half相同
    if k >= half:
        return solve(n - 1, k - half)
    # 和上一行的 k 取反
    else:
        return 1 if solve(n - 1, k) == 0 else 0

# 读取输入
t = int(sys.stdin.readline().strip())
for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())
    res = solve(n, k)
    print("red" if res == 0 else "blue")
