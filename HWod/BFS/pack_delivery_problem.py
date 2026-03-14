"""
思想: 对每个包裹跑一遍BFS, 看看能不能从起点到终点
      注意该题目的道路是双向的
"""
from collections import deque

def solve():
    M, N = map(int, input().split())

    packages = {}  # {包裹名: (起点, 终点)}
    for _ in range(M):
        parts = input().split()
        name, start, end = parts[0], parts[1], parts[2]
        packages[name] = (start, end)  # 集合只能赋值

    roads = []  # [(站点1, 站点2, {禁止通行的包裹})]
    for _ in range(N):
        parts = input().split()
        s1, s2 = parts[0], parts[1]
        blocked = set(parts[2:])
        roads.append((s1, s2, blocked))

    def can_deliver(pkg_name, start, end):
        # BFS，只走不禁止该包裹的道路
        visited = set([start])
        queue = deque([start])
        while queue:
            cur = queue.popleft()
            if cur == end:  # 已到达终点
                return True
            for s1, s2, blocked in roads:
                if pkg_name in blocked:
                    # 该道路禁止此包裹通行
                    continue  # 跳过后面代码, 开启下一次循环
                # 道路是双向的
                next = None
                if s1 == cur:
                    next = s2  # 移动到s2
                elif s2 == cur:  # 移动到s1
                    next = s1
                if next and next not in visited:
                    visited.add(next)
                    queue.append(next)
        return False

    failed = []  # 无法送达的包裹
    for name, (start, end) in packages.items():
        if not can_deliver(name, start, end):
            failed.append(name)

    if not failed:
        print("none")
    else:
        # 升序排列后输出
        failed.sort()
        print(" ".join(failed))

solve()