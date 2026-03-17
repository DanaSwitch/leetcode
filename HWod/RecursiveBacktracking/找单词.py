def dfs(n, x, y, target, k, path, visited, matrix):
    # 越界 | 已访问 | 首字符不匹配
    if (x < 0 or x >= n or y < 0 or y >= n
            or visited[x][y]
            or matrix[x][y][0] != target[k]):  # [0] 取首字符，兼容多余空白
        return False

    path.append((x, y))
    visited[x][y] = True

    if k == len(target) - 1:           # 已匹配最后一个字符
        return True

    for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
        if dfs(n, x+dx, y+dy, target, k+1, path, visited, matrix):
            return True

    # 回溯
    visited[x][y] = False
    path.pop()
    return False


def findPath(matrix, target):
    n = len(matrix)
    visited = [[False] * n for _ in range(n)]  # 共享布尔数组，回溯还原
    path = []
    for i in range(n):
        for j in range(n):
            if matrix[i][j][0] == target[0]:  # 外层前置过滤，减少无效调用
                if dfs(n, i, j, target, 0, path, visited, matrix):
                    return ",".join(f"{x},{y}" for x, y in path)
    return "N"


if __name__ == "__main__":
    n = int(input())
    matrix = [input().split(",") for _ in range(n)]
    target = input().strip()
    print(findPath(matrix, target))