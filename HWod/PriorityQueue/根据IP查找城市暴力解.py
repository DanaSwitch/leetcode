import sys
import heapq  # ★ 新增

def parse_ip(ip):
    parts = list(map(int, ip.strip().split('.')))
    res = 0
    for part in parts:
        res = (res << 8) | part
    return res

city_ip_line = sys.stdin.readline().strip()
search_ip_line = sys.stdin.readline().strip()

ip_ranges = []
for entry in city_ip_line.split(';'):
    city, ips = entry.split('=')
    start_ip, end_ip = ips.split(',')
    start = parse_ip(start_ip)
    end = parse_ip(end_ip)
    length = end - start + 1
    ip_ranges.append((start, end, length, city))

ip_ranges.sort()

search_ips = search_ip_line.split(',')
m = len(search_ips)
search_longs = [parse_ip(ip) for ip in search_ips]
q_index = sorted(range(m), key=lambda i: search_longs[i])

res = [''] * m

heap = []  # ★ candidates 换成堆
j = 0

for qi in q_index:
    target_ip = search_longs[qi]

    # 起点 <= target_ip 的段入堆（按长度排序, 堆顶最短）
    while j < len(ip_ranges) and ip_ranges[j][0] <= target_ip:
        start, end, length, city = ip_ranges[j]
        heapq.heappush(heap, (length, end, j))  # ★ 入堆
        j += 1

    # ★ 弹出终点 < target_ip 的过期段
    while heap and heap[0][1] < target_ip:
        heapq.heappop(heap)

    # ★ 堆顶直接就是最佳匹配, 不需要再遍历
    if heap:
        res[qi] = ip_ranges[heap[0][2]][3]

print(",".join(res))