"""
思路: 将地图所有位置初始化为0, 墙的位置初始化为1, 能到达终点的路径设为2
      不能到达终点的位置设置为-1, 陷阱就是-1的数量, 不可达就是0的数量
"""
import sys
sys.setrecursionlimit(2500)

x, y = map(int, input().split())  # 行, 列
n = int(input())  # 墙壁个数
poses = [list(map(int, input().split())) for _ in range(n)]

def dfs(cx, cy, grid):
    if cx >= x or cy >= y:
        return False
    if grid[cx][cy] == 1:  # 如果下一步为墙，则下一步不可达
        return False
    if grid[cx][cy] == -1:  # 如果下一步为不可达点，则下一步不可达
        return False
    if grid[cx][cy] == 2:   # 如果下一步为可达点，则下一步可达
        return True
    if grid[cx][cy] == 0:
        east = dfs(cx + 1, cy, grid)  # 向东走下一步
        north = dfs(cx, cy + 1, grid)  # 向北走下一步
        if east or north:
            grid[cx][cy] = 2  # 如果向东可达或者向北可达,则当前点可达,标记2
        else:
            grid[cx][cy] = -1  # 如果向东，向北都不可达，则当前前也是不可达点，标记-1
    return grid[cx][cy] == 2

def getResult():
    grid = [[0]*y for _ in range(x)]  # 初始化全部置0
    for i, j in poses:
        grid[i][j] = 1  # 墙标记为1
    grid[x - 1][y - 1] = 2  # 终点标记为2
    dfs(0, 0, grid)
    trap = 0  # 陷阱数量
    unreach = 0  # 不可达点数量
    for i in range(x):
        for j in range(y):
            if grid[i][j] == 0:
                unreach += 1
            elif grid[i][j] == -1:
                trap += 1
    return f"{trap} {unreach}"
# 算法调用
print(getResult())