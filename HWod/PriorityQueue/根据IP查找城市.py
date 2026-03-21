import sys
import heapq

# 第一步: 把 IP 地址变成数字 (parse_ip 函数)
def parse_ip(ip):
    parts = list(map(int, ip.strip().split('.')))
    res = 0  # 记录结果
    for part in parts:  # 从左往右
        res = (res << 8) | part  # 按位或, 进行拼接
    return res

city_ip_line = sys.stdin.readline().strip()
search_ip_line = sys.stdin.readline().strip()

# 解析城市 IP 段
ip_ranges = []
for entry in city_ip_line.split(';'):
    city, ips = entry.split('=')
    start_ip, end_ip = ips.split(',')
    start = parse_ip(start_ip)
    end = parse_ip(end_ip)
    ip_ranges.append((start, end, city))


# 第二步: 对城市 IP 段和查询 IP 进行排序（核心铺垫）
ip_ranges.sort()  # 按起始 IP 升序排序

# 查询 IP 转换为 long 并记录原始索引
search_ips = search_ip_line.split(',')
m = len(search_ips)
# 要搜索的ip字段的长整数
search_longs = [parse_ip(ip) for ip in search_ips]
# q_index 记录的是“排好序的IP, 在原来数组里的位置”
q_index = sorted(range(m), key=lambda i: search_longs[i])


# 第三步: 数轴漫游，也就是“扫描线 + 最小堆”
# 双指针 + 最小堆
# 按区间长度升序, 然后按 end 升序
heap = []
res = [''] * m
j = 0

for qi in q_index:
    ip_val = search_longs[qi]

    # 把所有起点 <= 当前 IP 的 IP 段入堆
    while j < len(ip_ranges) and ip_ranges[j][0] <= ip_val:
        start, end, city = ip_ranges[j]
        length = end - start + 1
        heapq.heappush(heap, (length, end, j))  # 保存 index 方便取 city
        j += 1

    # 移除无效段（end < ip_val）
    while heap and heap[0][1] < ip_val:
        heapq.heappop(heap)

    if heap:
        res[qi] = ip_ranges[heap[0][2]][2]  # 匹配城市

# 输出结果
print(",".join(res))