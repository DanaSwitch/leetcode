from collections import deque
import sys

applicants = []  # 应聘者
for line in sys.stdin:
    line = line.strip()

    if line == 'Exit':
        break
    line = line.split()
    id_, name, priority, order, count = line
    applicants.append({
            'id': id_,
            'name': name,
            'priority': priority == 'true',
            'order': int(order),
            'count': int(count),
            'had_count': 0  # 已经过好次数
    })

# 按照优先级和预约顺序来排序
applicants.sort(key = lambda x: (not x['priority'], x['order']))

queue = deque(applicants)

while queue:
    cur = queue.popleft()
    if cur['count'] > 0:  # 过号
        print(f"{cur['id']}:{cur['name']}:{'Y'}")
        cur['count'] -= 1
        cur['priority'] = False
        cur['had_count'] += 1
        # 第一次过号, 排到下一位
        step = min(len(queue), 1<<(cur['had_count'] - 1))
        queue.insert(step, cur)
    else:
        print(f"{cur['id']}:{cur['name']}:{'N'}")