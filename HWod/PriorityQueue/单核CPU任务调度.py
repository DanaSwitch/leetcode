import heapq
import sys

# 读入任务，每行：[id, 优先级, 执行时间, 到达时间]
tasks = [list(map(int, line.split())) for line in sys.stdin if line.strip()]

wait_queue = []  # 等待堆：(-优先级, 到达时间, tid, 剩余时间)
results = []
cur = None       # 当前运行任务：[tid, pri, remain, arrive]
t = 0            # 当前时间
i = 0            # 待读取的任务下标

while i < len(tasks) or cur or wait_queue:
    # 计算当前任务的完成时间
    finish_time = t + cur[2] if cur else float('inf')

    # 找最早的、能抢占当前任务的新到达任务
    preempt_time = finish_time
    for j in range(i, len(tasks)):
        if tasks[j][3] >= finish_time:  # 完成后才到
            break
        # 优先级更高, 抢占
        if tasks[j][1] > (cur[1] if cur else -1):
            preempt_time = tasks[j][3]
            break

    # 推进时间：取"完成"和"抢占"中较早的
    # CPU空闲则直接跳到下一任务到达
    prev_t = t
    t = min(finish_time, preempt_time) if cur else tasks[i][3]
    if cur:
        cur[2] -= t - prev_t   # 扣掉这段时间内消耗的执行时间

    # 将所有已到达的任务加入等待队列
    while i < len(tasks) and tasks[i][3] <= t:
        tid, pri, exe, arr = tasks[i]
        heapq.heappush(wait_queue, (-pri, arr, tid, exe))
        i += 1

    # 当前任务执行完毕
    if cur and cur[2] == 0:
        results.append((t, cur[0]))
        cur = None

    # CPU 空闲，或等待队列中存在更高优先级任务 → 重新调度
    if wait_queue and (not cur or -wait_queue[0][0] > cur[1]):
        if cur:  # 被抢占：将当前任务放回等待队列，原始到达时间用于同优先级排序
            heapq.heappush(wait_queue, (-cur[1], cur[3], cur[0], cur[2]))
        neg_pri, arr, tid, rem = heapq.heappop(wait_queue)
        cur = [tid, -neg_pri, rem, arr]

results.sort()
print('\n'.join(f'{tid} {t}' for t, tid in results))