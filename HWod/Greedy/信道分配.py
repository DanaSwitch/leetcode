"""
思路: 每个用户消耗的总容量 = 略大于等于 D 的最小值

"""
def solve():
    r = int(input())  # 最大阶数
    arr = list(map(int, input().split()))  # 信道数量
    d = int(input())  # 单用户数据量

    count = 0  # 用户数

    # 1. 单个信道容量 >= D，直接每个服务一个用户
    for i in range(r, -1, -1):  # r到0
        if (1 << i) >= d:
            count += arr[i]  # 加上数量
            arr[i] = 0

    # 2. 需要组合信道的情况
    while True:
        cur_sum = 0  # 每轮开始自动重置

        # 第一步: 从大到小, 只要不超过 D 就加
        for i in range(r, -1, -1):
            while arr[i] > 0 and cur_sum + (1 << i) < d:
                cur_sum += (1 << i)
                arr[i] -= 1

        # 第二步: 从小到大, 补到刚好 >= D
        for i in range(r + 1):
            while arr[i] > 0 and cur_sum < d:
                cur_sum += (1 << i)
                arr[i] -= 1

        if cur_sum >= d:
            count += 1
        else:
            break

    print(count)

solve()