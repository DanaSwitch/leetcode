import sys
import heapq

# 1. 读取所有输入数据 (OD机试处理多行输入的标准写法)
tasks = []
for line in sys.stdin:
    if line.strip(): 
        tasks.append(list(map(int, line.split())))

# 堆：存放正在等待/被抢占的任务
# 元素格式: (-priority, arrive_time, task_id, remain_time)
heap = []
current_time = 0
result = []

# 2. 遍历每一个新到达的任务
for task in tasks:
    task_id, priority, exec_time, arrive_time = task
    # 在新任务到达前, 处理掉堆里面可以执行的任务
    while heap and current_time < arrive_time:
        # 拿出当前优先级最高的任务
        p, a, tid, remain_time = heapq.heappop(heap)
        # 它可以执行的时间取决于：它自己还需要多久 vs 新任务还有多久到达
        run_time = min(remain_time, arrive_time - current_time)
        # 时间推进，任务剩余时间减少
        current_time += run_time
        remain_time -= run_time
        if remain_time == 0:
            # 任务执行完了，记录结束时间
            result.append((tid, current_time))
        else:
            # 任务还没执行完，但是新任务到来了（时间碰头了），被抢占，重新放回堆里
            heapq.heappush(heap, (p, a, tid, remain_time))
    current_time = max(current_time, arrive_time)
    heapq.heappush(heap, (-priority, arrive_time, task_id, exec_time))
# 3. 所有任务都已经到达, 不再有抢占, 把堆里剩下的任务依次执行完
while heap:
    p, a, tid, remain_time = heapq.heappop(heap)
    current_time += remain_time
    result.append((tid, current_time))
# 4. 输出结果 (由于我们是按照任务结束的瞬间存入result的，所以天生就是按结束时间排序的)
for tid, end_time in result:
    print(f"{tid} {end_time}")