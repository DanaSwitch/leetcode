import math

def solve():
    N = int(input())
    files = [int(input()) for _ in range(N)]

    CAPACITY = 1474560 // 512  # 2880 块

    # 每个文件：占用块数 & 实际大小
    items = []
    for s in files:
        blocks = math.ceil(s / 512)  # 占用块数（重量）
        items.append((blocks, s))    # (重量, 价值)

    # 0/1 背包 DP
    dp = [0] * (CAPACITY + 1)

    for blocks, value in items:
        if blocks > CAPACITY:
            continue
        # 从大到小遍历，保证每件物品只用一次
        for c in range(CAPACITY, blocks - 1, -1):
            dp[c] = max(dp[c], dp[c - blocks] + value)

    print(dp[CAPACITY])


solve()
