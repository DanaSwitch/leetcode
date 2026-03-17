def solve():
    R = int(input())  # 最大阶数
    pool = list(map(int, input().split()))  # 信道数量
    D = int(input())  # 单用户传输量

    # D 转二进制数组，低位在前。例：D=6=[1,1,0] 表示 0×1 + 1×2 + 1×4
    demand = []
    tmp = D
    while tmp:
        demand.append(tmp & 1)  # 取最低位
        tmp >>= 1
    n = len(demand)  # D 的二进制位数

    # 阶 >= n 的信道单个容量 2^r >= 2^n > D，一个信道直接服务一个用户
    users = sum(pool[r] for r in range(n, R + 1))

    # 只保留低阶部分，补齐长度到 n
    pool = pool[:n] + [0] * max(0, n - len(pool))

    def try_serve_one_user():
        """
        用二进制减法从 pool 中扣掉一个 D。
        成功返回 True, 信道不足返回 False。
        """
        for bit in range(n - 1, -1, -1):

            if pool[bit] >= demand[bit]:
                # 当前位够用，直接扣
                pool[bit] -= demand[bit]

            elif sum(pool[i] << i for i in range(bit + 1)) >= \
                 sum(demand[i] << i for i in range(bit + 1)):
                # 当前位不够，但低位总容量够
                # 把亏欠向低一位传递：欠 1 个 2^bit = 欠 2 个 2^(bit-1)
                pool[bit] -= demand[bit]       # 变为负数表示亏欠
                pool[bit - 1] += pool[bit] * 2 # 亏欠翻倍传给低一位
                pool[bit] = 0

            else:
                # 低位也不够，找一个更高阶的信道来顶
                for h in range(bit + 1, n):
                    if pool[h] > 0:
                        pool[h] -= 1
                        return True  # 高阶信道容量足以覆盖剩余所有需求
                return False  # 没有可用信道了

        return True

    while try_serve_one_user():
        users += 1

    print(users)

solve()