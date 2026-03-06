from collections import deque

# 1. 读取输入
n = int(input())
confirmed = list(map(int, input().replace(',', ' ').split()))

matrix = [list(map(int, input().replace(',', ' ').split())) for _ in range(n)]

# 2. BFS：从所有确诊者出发寻找传播链
# visited 初始化为所有确诊者
visited = set(confirmed)  # 集合记录感染者编号
queue = deque(confirmed)  # 以初始确诊者作为感染起点

while queue:
    person = queue.popleft()  # 将初始确诊者移出来
    for neighbor in range(n):
        # 如果存在接触关系且未被访问过，则加入扩散队列
        if matrix[person][neighbor] == 1 and neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)

# 3. 输出结果
# 总访问人数减去原始确诊人数，即为“需要检测”的人数
print(len(visited) - len(confirmed))