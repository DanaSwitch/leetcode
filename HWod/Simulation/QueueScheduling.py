from collections import deque

class Applicant:
    def __init__(self, id, name, priority, order, miss):
        self.id = id
        self.name = name
        self.priority = priority
        self.order = order
        self.miss = miss  # 过号次数
        self.orderMiss = 0  # 已经过号次数

applicants = []

while True:
    parts = input().split()
    if parts[0] == "Exit":  # 直到接收到"Exit"才退出
        break
    id, name, priorityStr, order, miss = parts  # 自动解包
    applicants.append(Applicant(id, name, priorityStr == "true", int(order), int(miss)))

# 按优先和预约顺序排序
applicants.sort(key=lambda x: ((not x.priority), x.order))  # not是倒序, True要排在False的前面

queue = deque(applicants)  #双端队列

while queue:  # 队伍有人
    cur = queue.popleft()  # 队首取出第一个人
    print(f"{cur.id}:{cur.name}:{'Y' if cur.miss > 0 else 'N'}")

    if cur.miss > 0:
        cur.orderMiss += 1
        cur.miss -= 1
        step = 1 << (cur.orderMiss - 1)
        step = min(step, len(queue))  # 不超过队列长度
        queue.insert(step, cur)  # 插入到退避步长位置

