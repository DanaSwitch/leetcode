import sys

def solve():
    # 1. 使用 sys.stdin.read() 一次性读取所有输入
    # .split() 会自动处理空格和换行，生成一个全是字符串的列表
    input_data = sys.stdin.read().split()

    if not input_data:
        return

    # 2. 创建一个迭代器，像指针一样方便我们需要时取下一个数据
    iterator = iter(input_data)

    # 依次取出 N, K, L
    N = int(next(iterator))
    K = int(next(iterator))
    L = int(next(iterator))

    # 接下来读取 N 个初始兵营人数
    # 列表推导式配合迭代器，快速生成列表
    camps = [int(next(iterator)) for _ in range(N)]

    # 3. 处理 L 条命令
    for _ in range(L):
        cmd_type = next(iterator) # 读取命令类型 (Add/Sub/Query)
        p1 = int(next(iterator))  # 读取 i
        p2 = int(next(iterator))  # 读取 j

        if cmd_type == 'Add':
            # i 对应的列表索引是 p1 - 1
            camps[p1 - 1] += p2

        elif cmd_type == 'Sub':
            camps[p1 - 1] -= p2

        elif cmd_type == 'Query':
            # Query i j: 查询从 i 到 j 范围内，连续 K 个兵营的最小和
            start_range = p1 - 1  # 范围起始索引
            end_range = p2 - 1    # 范围结束索引

            # --- 滑动窗口逻辑 ---
            
            # 计算第一个窗口的和 (起点是 start_range)
            current_sum = sum(camps[start_range : start_range + K])
            min_sum = current_sum

            # 窗口滑动的最后起点的索引
            # 假设范围是 [0, 4], K=2，最后一个窗口是 [3, 4]，起点是 3
            # 3 = 4 - 2 + 1
            limit = end_range - K + 1

            # 开始滑动
            # current_head 是窗口的【头】（左边第一个元素）的索引
            # 从第二个窗口开始滑，所以起点是 start_range + 1
            for current_head in range(start_range + 1, limit + 1):
                # 离开窗口的元素：是上一个窗口的头部 (current_head - 1)
                leaving_val = camps[current_head - 1]
                
                # 进入窗口的元素：是当前窗口的尾部
                # 当前头是 current_head, 长度 K, 尾部索引是 current_head + K - 1
                entering_val = camps[current_head + K - 1]

                # 更新窗口和：减去离开的，加上进来的
                current_sum = current_sum - leaving_val + entering_val

                if current_sum < min_sum:
                    min_sum = current_sum
            
            print(min_sum)


if __name__ == "__main__":
    solve()