import sys
sys.setrecursionlimit(2500)

# 输入获取
x, y = map(int, input().split())
n = int(input())
poses = [list(map(int, input().split())) for _ in range(n)]


# 深搜
def dfs(cx, cy, matrix):
    if cx >= x or cy >= y:
        return False
    if matrix[cx][cy] == 1:  # 如果下一步为墙，则下一步不可达
        return False
    if matrix[cx][cy] == -1:  # 如果下一步为不可达点，则下一步不可达
        return False
    if matrix[cx][cy] == 2:   # 如果下一步为可达点，则下一步可达
        return True
    if matrix[cx][cy] == 0:
        east = dfs(cx + 1, cy, matrix)  # 向东走下一步
        north = dfs(cx, cy + 1, matrix)  # 下北走下一步
        if east or north:
            matrix[cx][cy] = 2  # 如果向东可达或者向北可达，则当前点可达，标记2
        else:
            matrix[cx][cy] = -1  # 如果向东，向北都不可达，则当前前也是不可达点，标记-1
    return matrix[cx][cy] == 2

def getResult():
    matrix = [[0 for _ in range(y)] for _ in range(x)]
    for i, j in poses:
        matrix[i][j] = 1  # 墙标记为1，非墙标记为0
    matrix[x - 1][y - 1] = 2  # 可达点标记为2
    dfs(0, 0, matrix)
    trap = 0  # 陷阱数量
    unreach = 0  # 不可达点数量
    for i in range(x):
        for j in range(y):
            if matrix[i][j] == 0:
                unreach += 1
            elif matrix[i][j] == -1:
                trap += 1
    return f"{trap} {unreach}"
# 算法调用
print(getResult())