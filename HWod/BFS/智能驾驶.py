"""
有一辆汽车需要从 m * n 的地图左上角（起点）开往地图的右下角（终点），去往每一个地区都需要消耗一定的油量，加油站可进行加油。

请你计算汽车确保从从起点到达终点时所需的最少初始油量。

说明：

智能汽车可以上下左右四个方向移动
地图上的数字取值是 0 或 -1 或 正整数：
-1 :表示加油站, 可以加满油, 汽车的油箱容量最大为100
0 :表示这个地区是障碍物，汽车不能通过
正整数：表示汽车走过这个地区的耗油量
如果汽车无论如何都无法到达终点，则返回 -1
"""
import sys
from collections import deque


def can_reach(grid, m, n, initial_fuel):
    """
    判断以 initial_fuel 初始油量出发，能否到达右下角 (m-1, n-1)
    使用 BFS, max_fuel[i][j] 记录到达该格时的最大剩余油量（用于剪枝）
    """
    # 进入起点后的剩余油量
    if grid[0][0] == -1:
        start_fuel = 100  # 起点是加油站，直接加满
    else:
        start_fuel = initial_fuel - grid[0][0]

    if start_fuel < 0:
        return False

    # max_fuel[i][j] = 曾经到达 (i,j) 时的最大剩余油量，-1 表示未访问
    max_fuel = [[-1] * n for _ in range(m)]
    max_fuel[0][0] = start_fuel

    queue = deque()
    queue.append((0, 0, start_fuel))  # (坐标, 初始油量)
    DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        r, c, fuel = queue.popleft()
        # 当前状态已过期（该格已被更优路径更新）,跳过
        if fuel < max_fuel[r][c]:
            continue
        # 到达终点
        if r == m - 1 and c == n - 1:
            return True
        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            # 越界检查
            if not (0 <= nr < m and 0 <= nc < n):
                continue
            val = grid[nr][nc]
            # 障碍物，不能通过
            if val == 0:
                continue
            # 计算进入下一格后的剩余油量
            if val == -1:  # 加油站, 加满至100
                new_fuel = 100      
            else:
                new_fuel = fuel - val
            # 油量不足，无法进入
            if new_fuel < 0:
                continue
            # 剪枝：只有比之前到达该格的油量更多时，才值得入队
            if new_fuel > max_fuel[nr][nc]:
                max_fuel[nr][nc] = new_fuel
                queue.append((nr, nc, new_fuel))
    return False

def solve():
    data = sys.stdin.read().split()
    idx = 0
    mn = data[idx].split(',')
    m, n = int(mn[0]), int(mn[1])  # 行, 列
    idx += 1
    grid = []
    for _ in range(m):
        row = list(map(int, data[idx].split(',')))
        grid.append(row)
        idx += 1
    # 特判: 起点或终点是障碍
    if grid[0][0] == 0 or grid[m - 1][n - 1] == 0:
        print(-1)
        return
    # 先用满油（100）检查是否有可行路径
    if not can_reach(grid, m, n, 100):
        print(-1)
        return
    # 二分初始油量，范围 [0, 100]
    lo, hi = 0, 100
    ans = 100
    while lo <= hi:
        mid = (lo + hi) // 2
        if can_reach(grid, m, n, mid):
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1
    print(ans)

solve()