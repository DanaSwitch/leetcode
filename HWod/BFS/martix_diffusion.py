from collections import deque

line = list(map(int, input().strip().split(',')))
m, n = int(line[0]), int(line[1])  # 行, 列
i, j = int(line[2]), int(line[3])
k, l = int(line[4]), int(line[5])

martix = [[0] * n for _ in range(m)]
martix[i][j], martix[k][l] = 1,1
queue = deque()  # 已感染

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

queue.append((i, j))
queue.append((k, l))

time = 0  # 感染时间

while queue:
    for _ in range(len(queue)):
        x, y = queue.popleft()

        for dx, dy in dirs:
            new_x, new_y = x + dx, y + dy
            # x是行, y是列
            if 0 <= new_x < m and 0 <= new_y < n:  # 注意这里是小于m, n
                if martix[new_x][new_y] == 0:
                    martix[new_x][new_y] = 1
                    queue.append((new_x, new_y))
    # 每处理当前队列的所有感染点后, time就加一, 层次仅次于while queue
    time += 1

print(time-1)  # 扩散完成后, if判断没进去, 但是time还是会加1