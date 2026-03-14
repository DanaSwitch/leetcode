"""
思路: queue(坐标, 天数)
"""
from collections import deque

def solve(grid):
    rows = len(grid)
    cols = len(grid[0])
 
    queue = deque()
    no_count = 0

    # 初始化：收集所有YES坐标，统计NO数量
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "YES":
                queue.append((i, j, 0))  # (行, 列, 天数)
            elif grid[i][j] == "NO":
                no_count += 1

    # 如果没有NO，直接返回0
    if no_count == 0:
        return 0

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    days = 0

    while queue:
        x, y, day = queue.popleft()
 
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # 边界检查 + 只扩散到NO格子
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == "NO":
                grid[nx][ny] = "YES"
                no_count -= 1
                days = max(days, day + 1)
                queue.append((nx, ny, day + 1))

    return days if no_count == 0 else -1

# 读取输入
import sys

lines = []
for line in sys.stdin:
    line.strip()
    if line:
        lines.append(line.split())

print(solve(lines))