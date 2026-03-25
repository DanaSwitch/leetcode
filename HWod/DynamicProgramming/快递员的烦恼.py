from collections import defaultdict

n, m = map(int, input().split())  # n条起点到客户的距离, m条客户与客户之间的距离

dist = [[float('inf')] * (n + 1) for _ in range(n + 1)]
dic = defaultdict(int)

# n条起点到客户的距离
for i in range(1, n + 1):
    idx, dis = map(int, input().split())
    dic[idx] = i  # dic 将原始客户 id 映射为连续编号 1~n
    dist[0][i] = dist[i][0] = dis  # 无向图

#  m条客户与客户之间的距离
for _ in range(m):
    idx1, idx2, dis = map(int, input().split())
    i1, i2 = dic[idx1], dic[idx2]
    dist[i1][i2] = dist[i2][i1] = dis

def floyd():
    for k in range(n + 1):  # k是中转站
        for i in range(n + 1):
            for j in range(n + 1):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

ans = float('inf')
# 快递送完后要回到起点
def dfs(cur, sum_dist, used, level):
    global ans
    if level == n:
        ans = min(ans, sum_dist + dist[cur][0])
        return
    for i in range(1, n + 1):
        if not used[i]:
            used[i] = True
            dfs(i, sum_dist + dist[cur][i], used, level + 1)
            used[i] = False
    
floyd()
dfs(0, 0, [False] * (n + 1), 0)
print(ans)