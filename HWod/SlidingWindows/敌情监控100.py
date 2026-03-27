import sys

def solve():
    line1 = sys.stdin.readline().split()
    if not line1:
        return
    N, K, L = map(int, line1)  # 营地数, 兵营数, 命令数

    # 读取 camps 数组 (假设数据在第二行)
    camps = list(map(int, sys.stdin.readline().split()))

    # 处理 L 条命令
    for _ in range(L):
        line = sys.stdin.readline().split()
        if not line:
            break
            
        cmd_type = line[0]
        i = int(line[1])
        j = int(line[2])

        if cmd_type == 'Query':
            start = i - 1  # 转化为0开头
            end = j - 1
            
            # 计算第一个窗口的和(连续K个兵营数的和)
            cur_sum = sum(camps[start : start + K])
            min_sum = cur_sum
            # current + k - 1 <= end
            limit = end - K + 1

            # 滑动窗口
            for cur_head in range(start + 1, limit + 1):
                # 减去滑出的，加上滑入的
                cur_sum = cur_sum - camps[cur_head - 1] + camps[cur_head + K - 1]
                min_sum = min(cur_sum, min_sum)

            print(min_sum)

        elif cmd_type == 'Add':
            camps[i - 1] += j
        elif cmd_type == 'Sub':
            camps[i - 1] -= j

if __name__ == "__main__":
    solve()