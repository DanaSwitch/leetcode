from collections import deque
import sys

def solve():
    lines = sys.stdin.read().splitlines()
    lines = [l.strip() for l in lines if l.strip()]
    
    if len(lines) < 2:
        print(0)
        return

    modules = [x.strip() for x in lines[0].split(',')]
    node_id = {m: i for i, m in enumerate(modules)}
    n = len(modules)

    graph = [[] for _ in range(n)]
    in_degree = [0] * n

    for dep in lines[1].split(','):
        sep = '<-' if '<-' in dep else '<_'
        if sep not in dep:
            continue
        a, b = dep.split(sep)
        if a.strip() not in node_id or b.strip() not in node_id:
            continue
        u, v = node_id[b.strip()], node_id[a.strip()]
        graph[u].append(v)
        in_degree[v] += 1

    q = deque(i for i in range(n) if in_degree[i] == 0)
    removed = 0
    while q:
        u = q.popleft()
        removed += 1
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                q.append(v)

    print(n - removed)

solve()