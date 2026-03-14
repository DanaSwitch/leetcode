from collections import deque

def solve():
    m, n, k = map(int, input().split())

    grid = []
    for _ in range(m):
        row = list(map(int, input().split()))
        grid.append(row)

    dist = [[-1] * n for _ in range(m)]  # 从起点到每个格子的最短步数(格子数, 与山的高度无关)
    dist[0][0] = 0
    queue = deque()
    queue.append((0, 0))

    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    max_height = 0
    min_steps = 0

    while queue:
        x, y = queue.popleft()
        h = grid[x][y]  #当前山峰高度
        d = dist[x][y]  # 当前步数

        if h > max_height:
            max_height = h  # 更新最大高度
            min_steps = d   # 更新最短步数

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and dist[nx][ny] == -1:
                if abs(grid[nx][ny] - h) <= k:
                    dist[nx][ny] = d + 1
                    queue.append((nx, ny))

    print(max_height, min_steps)

solve()