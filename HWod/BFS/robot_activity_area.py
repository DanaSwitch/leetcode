"""
思路: 遍历所有节点, 不断更新最大活动区域
"""
from collections import deque

line = list(map(int, input().strip().split()))
m, n = int(line[0]), int(line[1])  # 行, 列

martix = []

for _ in range(m):
    row = list(map(int, input().split()))
    martix.append(row)

result = []
visited = [[False] * n for _ in range(m)]

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
max_area = 0  # 记录最大活动区域

for i in range(m):
    for j in range(n):
        if visited[i][j]:
            continue

        queue = deque([(i, j)])
        visited[i][j] = True
        area = 1
        while queue:
            r, c = queue.popleft()
            for dx, dy in dirs:
                new_x, new_y = r + dx, c + dy
                if 0 <= new_x < m and 0 <= new_y < n and not visited[new_x][new_y]:
                    diff = abs(martix[r][c] - martix[new_x][new_y])
                    if diff <= 1:
                        queue.append((new_x, new_y))
                        visited[new_x][new_y] = True
                        area += 1

        max_area = max(area,max_area)

print(max_area)