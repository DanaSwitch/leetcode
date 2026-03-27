"""
小明在出差期间使用便签记录行程，每条记录包含日期(yyyy-MM-dd格式)、城市和事件类型(到达arrive/离开leave)
现在他不小心把这些记录顺序打乱了, 请将这些打乱的记录重新排序, 按时间顺序输出他在每个城市的停留时间段。
规则:
1.输入的事件顺序为打乱的, 但每个城市的到达和离开事件总是成对出现且顺序合法
(在到达一个城市后，一定会先离开这个城市后才会有其他城市的到达记录)
2.同一天可能会包含多个城市的行程记录
3.同一个城市可能会有多组到达和离开记录，
同一个城市的多组到达离开记录需分开输出, 单天内如果同一城市有多组离开和到达记录，也需要分开输出

输入描述:
第一行为整数n, 表示记录的数量(1<n<1000)
接下来为n行记录, 格式为:日期城市名事件类型
其中:
日期为yyyy-MM-dd格式, 范围为2000-01-01到2030-01-01
城市名为大小写字母的组合, 字符串长度小于30, 城市名的首字母保
城市名：大小写字母的组合, 长度 < 30, 首字母大写
事件类型: arrive 或 leave

输出描述: 按时间先后顺序输出小明的每段行程
每行输出格式为: 城市名 到达日期 离开日期
如果在同一天内有多个行程，按实际发生的先后顺序输出


---
输入样例:
6
2023-05-10 Beijing arrive
2023-05-12 Shanghai arrive
2023-05-10 Beijing leave
2023-05-15 Shanghai leave
2023-05-10 Tokyo arrive
2023-05-10 Tokyo leave

输出样例:
Beijing 2023-05-10 2023-05-10
Tokyo 2023-05-10 2023-05-10
Shanghai 2023-05-12 2023-05-15
"""

from collections import defaultdict

n = int(input())
city_events = defaultdict(lambda : {'arrive': [], 'leave': []})
for _ in range(n):
    row = input().split()
    time, city, state = row[0], row[1], row[2]
    city_events[city][state].append(time)

# 城市内去留排序
arrive_leave = []
for city, events in city_events.items():
    arrives = sorted(events['arrive'])
    leaves = sorted(events['leave'])

    for arrive, leave in zip(arrives, leaves):
        arrive_leave.append((city, arrive, leave))

# 城市之间排序
arrive_leave.sort(key=lambda x: (x[1], x[2]))
for city, arrive, leave in arrive_leave:
    print(f"{city} {arrive} {leave}")