import sys
import heapq

def parse_input(s):
    s = s.strip()[2:-2]
    if not s:
        return []
    rows = s.split("],[")
    return [list(map(int, row.split(","))) for row in rows]

def dijkstra(grid, lights):
    m, n = len(grid), len(grid[0])  # 行, 列
    if grid[0][0] == 1 or grid[m-1][n-1] == 1:
        return -1

    # 二维: key直接用元组(x, y)
    light_map = {(x, y): t for x, y, t in lights}

    # 二维visited
    visited = [[float('inf')] * n for _ in range(m)]
    visited[0][0] = 0
    pq = [(0, 0, 0)]  # (time, x, y)

    while pq:
        time, x, y = heapq.heappop(pq)
        if time > visited[x][y]:  # 剪枝：跳过过期状态
            continue
        if x == m - 1 and y == n - 1:  # 到达终点
            return time

        next_time = time + 1
        if grid[x][y] == 2:  # 红绿灯
            next_time += light_map.get((x, y), 0)  # 没有就返回0

        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx, ny = x + dx, y + dy
            # 越界
            if not (0 <= nx < m and 0 <= ny < n):
                continue
            # 遇到障碍, 或没有更优解
            if grid[nx][ny] == 1 or visited[nx][ny] <= next_time:
                continue
            visited[nx][ny] = next_time
            heapq.heappush(pq, (next_time, nx, ny))

    return -1

if __name__ == '__main__':
    grid = parse_input(sys.stdin.readline())
    lights = parse_input(sys.stdin.readline())
    print(dijkstra(grid, lights))