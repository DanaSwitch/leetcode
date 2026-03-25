from collections import deque

N, K = map(int, input().split())  # 总共N, 可选K
security = []
for _ in range(N):
    security.append(int(input()))

M = int(input())  # m条道路
# path[i] = []
path = [[] for _ in range(N)]   # N 个[]
for _ in range(M):
    a, b = map(int, input().split())
    path[a].append(b)
    path[b].append(a)

def can_reach(limit):
    queue = deque()
    queue.append(0)  # 起点
    dist = [-1] * N  # dist[i] 表示0到i经过多少城市
    dist[0] = 1
    
    if security[0] < limit or security[N-1] < limit:
        return False
    
    while queue:
        cur  = queue.popleft()
        if cur == N-1:
            return dist[cur] <= K
        for next in path[cur]:
            if dist[next] == -1 and security[next] >= limit:
                dist[next] = dist[cur] + 1
                if dist[next] <= K:
                    queue.append(next)
    return False

low, high = min(security), max(security)
ans = -1

# 找更大
while low <= high:
    mid = (low + high)//2
    if can_reach(mid):
        ans = mid
        low = mid + 1
    else:
        high = mid - 1

print(ans)