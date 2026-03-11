"""
思路: 贪心算法, 按照积分排序, 在T时间内, 从大到小一个个完成
"""
N = int(input())
T = int(input())
tasks = [tuple(map(int, input().split())) for _ in range(N)]  # (最晚时间, 积分)

tasks.sort(key=lambda x: -x[1])
used = [False] * (T + 1)
total = 0

for last_time, point in tasks:
    for t in range(min(last_time, T), 0, -1):
        if not used[t]:
            used[t] = True
            total += point
            break

print(total)