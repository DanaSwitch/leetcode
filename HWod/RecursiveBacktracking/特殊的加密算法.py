import sys

# 读取输入
n = int(input())  # 明文长度
data = list(map(int, input().split()))  # 明文
m = int(input())  # 矩阵长度
book = [list(map(int, input().split())) for _ in range(m)]

directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
min_path = None  # 存储找到的字典序最小的密文路径
found = False  # 标记是否找到至少一种加密方式

def dfs(data, index, x, y, visited, path):
    global min_path, found
    if index == len(data):  # 如果已经处理完所有明文数字
        # 如果找到的是第一种加密方式, 或者字典序比之前的小
        if not found or path < min_path:  
            min_path = path  # 更新最小字典序密文路径
        found = True
        return
    # 如果坐标越界, 或该位置已访问, 或该位置数字与明文不匹配, 则返回
    if x < 0 or y < 0 or x >= m or y >= m or visited[x][y] or book[x][y] != data[index]:
        return

    visited[x][y] = True  # 标记当前位置已访问
    new_path = path + f"{x} {y} "  # 更新路径字符串, 带空格

    for dir in directions:  # 遍历四个方向
        newX, newY = x + dir[0], y + dir[1]
        dfs(data, index + 1, newX, newY, visited, new_path)

    visited[x][y] = False  # 回溯，撤销当前位置的访问标记

visited = [[False for _ in range(m)] for _ in range(m)]  # 标记密码本中的数字是否已经被访问过
for i in range(m):
    for j in range(m):
        if book[i][j] == data[0]:  # 从找到的第一个数字开始搜索
            dfs(data, 0, i, j, visited, "")  # 使用深度优先搜索找到所有可能的加密路径
# 如果找到至少一种加密方式，输出最小字典序的密文；否则，输出"error"
print(min_path.strip() if found else "error")  