"""
思路: 遍历网格中的所有'O'点, 找出只有一个边界入口的点
"""
from collections import deque

def solve():
    m, n = map(int, input().split())
    grid = []
    for _ in range(m):
        row = input().split()
        grid.append(row)
    
    visited = [[False] * n for _ in range(m)]
    result = []  # 全局变量(大小, 入口行, 入口列)
    
    for i in range(m):
        for j in range(n):
            # 遍历网格中的所有'O'点, 找出只有一个边界入口的点
            if grid[i][j] == 'O' and not visited[i][j]:  # 此处空闲且没被访问
                # BFS 找连通分量
                queue = deque([(i, j)])  # 在for下面, 每次遍历就更新
                visited[i][j] = True
                cells = []  # 记录连通点
                start = []  # 边界入口
                
                while queue:
                    r, c = queue.popleft()
                    cells.append((r, c))
                    # 判断是否在矩阵边界
                    if r == 0 or r == m - 1 or c == 0 or c == n - 1:
                        start.append((r, c))
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] == 'O':
                            visited[nr][nc] = True
                            queue.append((nr, nc))
                
                # 恰好只有 1 个边界入口 → 单入口空闲区域
                if len(start) == 1:
                    er, ec = start[0]
                    result.append((er, ec, len(cells)))
    
    if not result:
        print("NULL")
        return
    
    max_size = max(r[2] for r in result)
    max_regions = [r for r in result if r[2] == max_size]
    
    if len(max_regions) == 1:
        er, ec, size = max_regions[0]
        print(er, ec, size)
    else:
        # 多个最大区域大小相同，只输出大小
        print(max_size)

solve()