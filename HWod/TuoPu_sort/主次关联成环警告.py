import sys
from collections import defaultdict, deque

parent_map = defaultdict(set)
adj = defaultdict(list)
all_nodes = set()

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    parent, child = line.split()
    parent_map[child].add(parent)
    adj[parent].append(child)
    all_nodes.add(parent)
    all_nodes.add(child)

# ---------- 情况1：多个主告警 ----------
multi_parent = []

for child in parent_map:
    if len(parent_map[child]) > 1:
        multi_parent.append(child)

if multi_parent:
    multi_parent.sort()
    res = ",".join(multi_parent)
    print(f"[1001,({res})]")
    sys.exit(0)

# ---------- 情况2：检测环 ----------
indegree = defaultdict(int)

for parent in adj:
    for child in adj[parent]:
        indegree[child] += 1

queue = deque()

for node in all_nodes:
    if indegree[node] == 0:
        queue.append(node)

count = 0

while queue:
    node = queue.popleft()
    count += 1
    for child in adj[node]:
        indegree[child] -= 1
        if indegree[child] == 0:
            queue.append(child)

# 如果拓扑排序数量 < 节点数，则有环
if count < len(all_nodes):
    print("[1002,cycle]")
else:
    print("[1003,Verified]")