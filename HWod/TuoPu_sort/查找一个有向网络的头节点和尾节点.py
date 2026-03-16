from collections import deque

def solve():
    n = int(input())
    
    if n == 0:
        print()
        return
    
    nums = list(map(int, input().split()))
    edges = [(nums[i], nums[i+1]) for i in range(0, 2*n, 2)]
    
    # 收集所有节点
    all_nodes = set()
    for u, v in edges:
        all_nodes.add(u)
        all_nodes.add(v)
    
    # 构建原始数据（全程不动）
    in_deg = {node: 0 for node in all_nodes}
    out_deg = {node: 0 for node in all_nodes}
    graph = {node: [] for node in all_nodes}
    
    for u, v in edges:
        in_deg[v] += 1
        out_deg[u] += 1
        graph[u].append(v)
    
    # Kahn算法用副本，检测环
    kahn_in_deg = dict(in_deg)  # 浅拷贝
    queue = deque([node for node in all_nodes if kahn_in_deg[node] == 0])
    visited_count = 0
    
    while queue:
        node = queue.popleft()
        visited_count += 1
        # 删除该点后, 该点指向点的入度都减1
        for neighbor in graph[node]:
            kahn_in_deg[neighbor] -= 1
            if kahn_in_deg[neighbor] == 0:
                queue.append(neighbor)
    
    # 有环
    if visited_count != len(all_nodes):
        print(-1)
        return
    
    # 用原始 in_deg / out_deg 找头尾节点
    head_nodes = [node for node in all_nodes if in_deg[node] == 0]  # 头节点
    tail_nodes = sorted([node for node in all_nodes if out_deg[node] == 0])  # 尾节点
    
    print(*head_nodes, *tail_nodes)

solve()