import heapq
import sys

def solve():
    data = sys.stdin.read().split()
    idx = 0  # 索引
    m = int(data[idx]); idx += 1  # 缓存容量
    n = int(data[idx]); idx += 1  # 文件操作个数

    cache = {}   # fname: [size, count, time]
    used  = 0  # 已占用空间
    timer = 0  # 记录时间
    # 先删除访问次数少的, 时间久的
    heap  = []   # (count, time, fname)

    for _ in range(n):
        op = data[idx]; idx += 1

        if op == 'get':  # 读文件
            fname = data[idx]; idx += 1
            if fname in cache:
                timer += 1
                cache[fname][1] += 1  # 访问次数加一
                cache[fname][2]  = timer
                # 旧条目留在堆里自动过期，push新条目
                heapq.heappush(heap, (cache[fname][1], cache[fname][2], fname))

        elif op == 'put':  # 放文件
            fname = data[idx]; idx += 1
            fsize = int(data[idx]); idx += 1

            if fname in cache:  # 已存在
                continue

            # 淘汰阶段
            while used + fsize > m and heap:
                count, time, evict = heapq.heappop(heap)
                # 判断弹出来的数据是不是过时的
                # 名字都没了, 说明被删了
                if evict not in cache:
                    continue  # 已被淘汰
                # 名字在, 但是时间/次数对不上, 说明是假的
                if cache[evict][1] != count or cache[evict][2] != time:
                    continue  # get后产生的旧条目

                # 有效淘汰
                used -= cache[evict][0]
                del cache[evict]

            if used + fsize <= m:
                timer += 1  # 访问次数加一
                # 第一次放, 访问次数是0
                cache[fname] = [fsize, 0, timer]
                used += fsize  # 增加已使用空间
                heapq.heappush(heap, (0, timer, fname))  # 压入小根堆

    print(','.join(sorted(cache)) if cache else 'NONE')

solve()
