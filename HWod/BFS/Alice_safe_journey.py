from collections import deque

def solve():
    N, K = map(int, input().split())  # 城市总数, 可去的城市数
    
    h = []  # 记录每个城市的安全度
    for _ in range(N):
        h.append(int(input()))
    
    M = int(input())  # 城市道路数
    
    path = [[] for _ in range(N)]
    for _ in range(M):
        s0, s1 = map(int, input().split())
        path[s0].append(s1)  # 每个城市创建一个列表, 存放能直接到达的城市
        path[s1].append(s0)
    
    def can_reach(limit):
        if h[0] < limit or h[N-1] < limit:
            # 起点/终点 不满足
            return False
        
        dist = [-1] * N  # dist[i] 表示从城市0到城市i经过的城市数量
        dist[0] = 1
        queue = deque()
        queue.append([0])  # 从城市0出发
        
        while queue:
            cur = queue.popleft()
            if cur == N - 1:  # 到达终点
                return dist[cur] <= K
            for next in path[cur]:
                # next没去过且安全值满足
                if dist[next] == -1 and h[next] >= limit:
                    dist[next] = dist[cur] + 1
                    if dist[next] <= K:
                        queue.append(next)
        
        return False
    
    low, high = 0, max(h)
    ans = -1  # 安全度
    
    while low <= high:
        mid = (low + high) // 2
        if can_reach(mid):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    
    print(ans)

solve()