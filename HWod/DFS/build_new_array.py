def solve():
    N = list(map(int, input().split()))
    M = int(input())

    N_sorted = sorted(set(N))
    min_n = N_sorted[0]
    count = [0]  # int不可变, count可变

    def dfs(start, remaining):
        """从 N_sorted[start:] 中重复取数，凑出 remaining"""
        if remaining == 0:
            count[0] += 1
            return
        for i in range(start, len(N_sorted)):
            if N_sorted[i] > remaining:  # 剪枝
                break
            dfs(i, remaining - N_sorted[i])  # i 不变，允许重复取

    # Case 1：全部用 N 中的元素
    dfs(0, M)

    # Case 2：恰好用 1 个额外元素 j（1 <= j < min_n）
    for j in range(1, min_n):
        if j <= M:
            dfs(0, M - j)  # 额外元素最小，固定放在最前，剩余用 N 凑

    print(count[0])

solve()