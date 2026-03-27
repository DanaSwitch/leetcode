import heapq
from collections import defaultdict

n = int(input().strip())
records = []
for _ in range(n):
    row = input().split()
    records.append(row)

printers = defaultdict(list)  # {1:[], 2:[]}
# (-优先级, 时间)
file_id = 0
for record in records:
    if len(record) == 3:
        state, p, priority = record
        priority = int(priority)
        file_id += 1
        heapq.heappush(printers[p], (-priority, file_id))
    else:
        state, p = record
        if printers[p]:
            _, f_id = heapq.heappop(printers[p])
            print(f_id)
        else:
            print("NULL")
        