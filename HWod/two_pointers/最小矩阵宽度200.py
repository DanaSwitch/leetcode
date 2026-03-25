from collections import defaultdict, Counter

N, M = map(int, input().split())  # 行, 列
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))
K = int(input())
arr = list(map(int, input().split()))
required = Counter(arr)          # 需求频次
total_needed = len(required)     # 需满足的不同数字种数
# 按照列展开
cols = [[matrix[r][c] for r in range(N)] for c in range(M)]
window_count = defaultdict(int)
satisfied = 0   # 当前已满足的种数
min_width = float('inf')
l = 0
for r in range(M):
    # 右边界扩展：加入第 r 列
    for val in cols[r]:
        if val in required:
            window_count[val] += 1
            if window_count[val] == required[val]:
                satisfied += 1
    # 尝试收缩左边界
    while satisfied == total_needed:
        min_width = min(min_width, r - l + 1)
        # 移除第 l 列
        for val in cols[l]:
            if val in required:
                if window_count[val] == required[val]:
                    satisfied -= 1
                window_count[val] -= 1
        l += 1
print(min_width if min_width != float('inf') else -1)