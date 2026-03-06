import heapq

n = int(input())

# 5台打印机的队列，每台是一个堆
# 堆中元素格式: (-优先级, 入队序号, 文件编号)
# -优先级: heapq是最小堆，取负数就能实现"优先级越大越先出"
# 入队序号: 优先级相同时，序号小的先出（即最早入队）
printers = {i: [] for i in range(1, 6)}

file_id = 0       # 文件编号计数器（每次IN事件+1）
order = 0         # 入队顺序计数器（用于同优先级排序）

for _ in range(n):
    line = input().split()
    
    if line[0] == "IN":
        p = int(line[1])  # 打印机的序号
        num = int(line[2])  # 优先级
        file_id += 1
        order += 1
        # 入堆: (-优先级, 入队顺序, 文件编号)
        heapq.heappush(printers[p], (-num, order, file_id))  # 三个参数从左到右依次比较, 作为元组加入队列
    
    elif line[0] == "OUT":
        p = int(line[1])
        if printers[p]:  # 打印机不空
            # 取出堆顶（优先级最高、最早入队）
            _, _, fid = heapq.heappop(printers[p])
            print(fid)
        else:
            print("NULL")