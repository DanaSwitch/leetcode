import sys
import heapq

def ip_int(ip_str):
    a,b,c,d = map(int, ip_str.split('.'))
    return (a<<24)|(b<<16)|(c<<8)|d

city_ip_str = sys.stdin.readline().strip().split(';')
target_ip_str = sys.stdin.readline().strip().split(',')

all_ips = []  # (开始, 结束, 城市)
for record in city_ip_str:
    city, ips = record.split('=')
    start, end = ips.split(',')
    start = ip_int(start)
    end = ip_int(end)
    all_ips.append((start, end, city))

# 按照起点排序
all_ips.sort()

# 查询ip转为整数
n = len(target_ip_str)
search_vals = [ip_int(ip) for ip in target_ip_str]
# 保存下标
search_idx = sorted(range(n), key= lambda i: search_vals[i])

# 开始查询
heap = []  # (区间长度, 终点, all_ips下标)
res = ['']*n
j = 0  # 扫描all_ips
for idx in search_idx:
    target = search_vals[idx]

    # 先把所有起点 < target的城市入堆
    while j < len(all_ips) and all_ips[j][0] <= target:
        s, e, c = all_ips[j]
        heapq.heappush(heap, ((e-s), e, j))
        j += 1
    
    # 把终点 < target的堆顶弹出来
    while heap and heap[0][1] < target:
        heapq.heappop(heap)
    # 如果有的话
    if heap:
        res[idx] = all_ips[heap[0][2]][2]  # 记录城市名

print(','.join(res))