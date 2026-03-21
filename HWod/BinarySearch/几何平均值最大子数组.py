import sys
import math

def solve():
    data = sys.stdin.read().split()
    ptr = 0
    N = int(data[ptr]); ptr += 1  # numbers大小
    L = int(data[ptr]); ptr += 1  # 数组最小长度
    nums = [float(data[ptr + i]) for i in range(N)]
    log_nums = [math.log(x) for x in nums]  # 取对数
    # 前缀和: P[i] = log_nums[0] + ... + log_nums[i-1]
    P = [0.0] * (N + 1)
    for i in range(N):
        P[i + 1] = P[i] + log_nums[i]

# ── 阶段一: 二分搜索最大 log 平均值 v ──────────────────────────────────
    low, high = min(log_nums), max(log_nums)
    for _ in range(300):  # 300 次后精度 ≈ 10^{-88}, 远超需求
        mid = (low + high) * 0.5
        i_bound = 0  # 当前最新合法的i
        min_Q = 0.0   # i=0, Q[0] = P[0] − mid·0 = 0
        feasible = False
        i_bound = 0
        min_Q = 0.0
        feasible = False
        for j in range(L, N + 1):
            Qj = P[j] - mid * j
            if Qj >= min_Q - 1e-13:
                feasible = True
                break
            i_bound += 1  # i+1, 为后面的j做准备
            Qi_new = P[i_bound] - mid * i_bound
            min_Q = min(min_Q, Qi_new)
        if feasible:
            low = mid
        else:
            high = mid
    v = low   # 最大 log 均值的下确界（与真值偏差 < 10^{-88}）

# ── 阶段二: 寻找最短（再最靠前）的最优子数组 ─────────────────────────
    EPS = 1e-11
    threshold_base = v - EPS   # 存储 v−ε, 避免重复计算
    max_k = min(2 * L, N + 1)  # range 上界, 对应长度 L … 2L−1
    for k in range(L, max_k):  # 选k个数
        threshold = threshold_base * k
        for i in range(N - k + 1):
            if P[i + k] - P[i] >= threshold:
                print(i, k)
                return
    # 理论上不会到达此处
    print(0, L)

solve()