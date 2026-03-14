from collections import deque

def bfs():
    line1 = input().split()
    m, n = int(line1[0]), int(line1[1])
    line2 = input().split()
    row, col = int(line2[0]), int(line2[1])

    martix = []
    for i in range(row):
        tmp = list(map(int, input().strip().split()))
        martix.append(tmp)

    visited = [[False] * col for _ in range(row)]
    visited[0][0] = True

    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 上下左右

    queue = deque()
    queue.append([0,0,0])  # (坐标, 步数)

    while queue:
        r, c, steps = queue.popleft()  # 队列先进先出使用popleft
        if r == m and c == n:
            print(steps)
            return

        for dx, dy in dirs:
            new_x, new_y = r + dx, c + dy
            if 0 <= new_x < row and 0 <= new_y < col and not visited[new_x][new_y] and martix[new_x][new_y] == 0:
                visited[new_x][new_y] = True
                queue.append([new_x, new_y, steps+1])
    print(-1)

if __name__ == "__main__":
    bfs()