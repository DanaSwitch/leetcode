from collections import deque

line = list(map(int, input().strip().split()))
m, n, k = int(line[0]), int(line[1]), int(line[2])  # 行, 列

visited = [[False] * n  for _ in range(m)]
visited[0][0] = True

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

queue = deque()
queue.append((0, 0))

count = 1  # 黄金数, 从(0, 0)开始拿

# 计算数位之和
def get_digit_sum(num):
    sum = 0
    while num > 0:
        sum += num % 10  # 剩下个位
        num = num // 10  # 整除10
    return sum

while queue:
    x, y = queue.popleft()
    for dx, dy in dirs:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < m and 0 <= new_y < n and not visited[new_x][new_y]:
            if get_digit_sum(new_x) + get_digit_sum(new_y) <= k:
                visited[new_x][new_y] = True
                queue.append((new_x, new_y))
                count += 1
print(count)