"""
注意: 赋值的时候一定要注意列表和列表的值
last[1] 而不是 last
"""
import sys

n = int(sys.stdin.readline().strip())  # 会议数量
lines = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().strip().split())
    lines.append([a, b])

# 思路: max(起点) < min(终点): 合并
sort_lines = sorted(lines, key= lambda x: x[0])

result = []
result.append(sort_lines[0])

for start, end in sort_lines[1:]:
    last = result[-1]  # 最后时间
    if start <= last[1]:  # 合并
        last[1] = max(end, last[1])
    else:
        result.append([start, end])

for start, end in result:
    print(start, end)  # 默认空格分隔