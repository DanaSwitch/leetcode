from collections import deque

def solve():
    n, m = map(int, input().split())
    grid = []
    for _ in range(n):
        row = list(map(int, input().split()))
        grid.append(row)
    
    visited = [[False] * m for _ in range(n)]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    def bfs(r, c):
        queue = deque([(r, c)])
        visited[r][c] = True
        count = 1
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == 1:
                    visited[nx][ny] = True
                    count += 1
                    queue.append((nx, ny))
        return count
    
    max_count = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and not visited[i][j]:
                size = bfs(i, j)
                max_count = max(max_count, size)
    
    print(max_count)

solve()