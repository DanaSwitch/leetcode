import sys
from collections import deque

# 行, 列
rows, cols = map(int, sys.stdin.readline().split())

# 读取一维数组数据并记录信号源
grid = list(map(int, sys.stdin.readline().split()))
queue = deque()

for i in range(rows * cols):
    if grid[i] > 0:
        # 添加二维坐标
        queue.append((i // cols, i % cols))

# 方向数组：上、下、左、右
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 广度优先搜索 (BFS) 传播信号
while queue:
    x, y = queue.popleft()
    # 注意cols是每行有多少元素, 不用加1
    current_signal = grid[x * cols + y]
    # 这个信号再传就是0, 外面都是0, 不用继续
    if current_signal == 1:
        continue

    for dx, dy in dirs:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x * cols + new_y] == 0:
            # 空地, 信号减1
            grid[new_x * cols + new_y] = current_signal - 1
            queue.append((new_x, new_y))

# 读取目标坐标
target_x, target_y = map(int, sys.stdin.readline().split())
print(grid[target_x * cols + target_y])