from collections import defaultdict, deque

def solve():
    line1 = input().split()
    N, T = int(line1[0]), int(line1[1])  # 节点数, 列表数
    
    graph = defaultdict(list)  # 双向邻接表
    for _ in range(T):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    src = int(input())  # 广播节点号
    
    # BFS 求最短路
    dist = [-1] * (N + 1)
    dist[src] = 0  # dist[i]表示源节点到节点 i 的最短距离
    q = deque([src])
    
    while q:
        node = q.popleft()
        for next_node in graph[node]:
            if dist[next_node] == -1:
                dist[next_node] = dist[node] + 1
                q.append(next_node)
    
    # 最远距离 × 2（来回）
    print(max(dist[1:]) * 2)

solve()