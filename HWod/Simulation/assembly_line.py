"""
思路: 使用优先队列, 这样heap.heappop(pq)方便找到最快结束的流水线
      找到后将新的作业压进去, 不断更新最开始的最长作业时间和后面新压入作业的时间
"""

import heapq

m, n = map(int, input().split())  # 流水线个数, 作业数
lines = list(map(int, input().strip().split()))

lines.sort()
pq = []
res = 0  # 记录最长时间  
for i in range(n):
    if i < m:  # 直接入队
        heapq.heappush(pq, lines[i])
        res = max(res, lines[i])
    else:
        least_time = heapq.heappop(pq)  # 弹出时间最短的
        least_time += lines[i]  # 加上
        heapq.heappush(pq, least_time)  # 塞回去
        res = max(res, least_time)
print(res)