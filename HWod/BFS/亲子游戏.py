from collections import deque

def solve():
    n = int(input())
    grid = []
    mom = baby = None
    for i in range(n):
        row = list(map(int, input().split()))
        grid.append(row)
        for j, v in enumerate(row):
            if v == -3: mom = (i, j)  # 妈妈坐标
            elif v == -2: baby = (i, j)  # 宝宝坐标

    INF = float('inf')
    dist = [[INF]*n for _ in range(n)]
    candy = [[-1]*n for _ in range(n)]

    sr, sc = mom
    dist[sr][sc] = 0  # 妈妈到达(r, c)的最短步数
    candy[sr][sc] = 0  # 在最短步数前提下拿到的最多糖果

    queue = deque()
    queue.append((sr, sc))
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]

    while queue:
        r, c = queue.popleft()
        for dr, dc in dirs:
            nr, nc = r+dr, c+dc
            # 开始扩散
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] != -1:
                cell_candy = grid[nr][nc] if grid[nr][nc] >= 0 else 0
                new_dist = dist[r][c] + 1
                new_candy = candy[r][c] + cell_candy
                # 路径更短, 更新路径和糖果数
                if new_dist < dist[nr][nc]:
                    dist[nr][nc] = new_dist
                    candy[nr][nc] = new_candy
                    queue.append((nr, nc))
                # 路径相等, 只更新糖果数
                elif new_dist == dist[nr][nc] and new_candy > candy[nr][nc]:
                    candy[nr][nc] = new_candy
                    queue.append((nr, nc))

    br, bc = baby
    print(candy[br][bc] if dist[br][bc] != INF else -1)

solve()