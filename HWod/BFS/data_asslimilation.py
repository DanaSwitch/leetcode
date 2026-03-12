import sys
from collections import deque

def bfs(matrix, m, n):
    # 方向: 上下左右
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    matrix[0][0] = 1  # 起点
    queue = deque([(0, 0)])  # 存入坐标队()

    while queue:
        x, y = queue.popleft()  # 遍历一个淘汰一个
        # 上下左右扩散
        for dx, dy in direction:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < m and 0 <= new_y < n and matrix[new_x][new_y] == 0:
                matrix[new_x][new_y] = 1
                queue.append((new_x, new_y))


if __name__ == "__main__":
    m, n = map(int, sys.stdin.readline().strip().split())  # 行列

    martix = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(m)]

    bfs(martix, m, n)
    result = 0
    for row in martix:
        for col in row:
            if col != 1:
                result += 1
    print(result)
