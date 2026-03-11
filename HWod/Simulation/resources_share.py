import sys

n, m = map(int, sys.stdin.readline().split())  # n台设备, m次操作
free = [0] + list(map(int, input().split()))  # 1-indexed 设备资源数
alloc = []  # 记录每次申请的 (设备ID, 分配量)
result = []

for _ in range(m):
    type, x = map(int, input().strip().split())

    if type == 1:  # 申请资源
        # Best Fit: 找满足条件中剩余最少的设备（ID最小优先）
        candidates = [(free[i] - x, i) for i in range(1, n+1) if free[i] >= x]
        bestID = min(candidates)[1] if candidates else 0  # [1]提取出id
        if bestID:
            free[bestID] -= x
        alloc.append((bestID, x))
        result.append(bestID)

    else:
        # 释放第x次申请的资源
        id, num = alloc[x-1] if x <= len(alloc) else (0, 0)
        if id:
            free[id] += num

print(" ".join(map(str, result)))