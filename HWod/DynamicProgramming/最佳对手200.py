import sys

n, d = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

dp = [0] * (n + 1)
minSum = [0] * (n + 1)

for i in range(2, n + 1):
    diff = arr[i-1] - arr[i-2]

    # 方案A：第i支队伍不配对，继承i-1的结果
    A_pairs = dp[i-1]
    A_sum   = minSum[i-1]

    # 方案B：第i支与第i-1支配对，基于i-2的结果+1组
    if diff <= d:
        B_pairs = dp[i-2] + 1
        B_sum   = minSum[i-2] + diff
    else:
        B_pairs = -1              # 无法配对，设为-1表示不可用
        B_sum   = float('inf')   # 无法配对，差值和设为无穷大

    # 优先配对数多的，配对数相同取差值和小的
    if B_pairs > A_pairs:
        dp[i], minSum[i] = B_pairs, B_sum
    elif A_pairs > B_pairs:
        dp[i], minSum[i] = A_pairs, A_sum
    else:
        dp[i], minSum[i] = A_pairs, min(A_sum, B_sum)

print(-1 if dp[n] == 0 else minSum[n])