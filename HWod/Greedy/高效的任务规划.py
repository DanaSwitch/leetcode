# -*- coding: utf-8 -*-
def get_min_time(tasks):
    # 贪心：运行时间长的任务优先执行
    tasks.sort(key=lambda x: -x[1])
    # 获取最大执行结束时间
    res = 0
    last_config_end_time = 0
    for config_time, run_time in tasks:
        last_config_end_time += config_time
        res = max(res, last_config_end_time + run_time)
    return res

m = int(input())
for _ in range(m):
    n = int(input())
    tasks = [tuple(map(int, input().split())) for _ in range(n)]
    res = get_min_time(tasks)
    print(res)
