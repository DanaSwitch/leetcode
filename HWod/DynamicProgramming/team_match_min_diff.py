# 输入获取
import sys

n, d = map(int, input().split())  # n是队伍个数, d是允许的实力差值
arr = list(map(int, input().split()))


# segment: 差值数组; index: 当前处理到的下标; abandon: 是否已经舍弃过一个队; 
# total: 当前累计差值和; minTotal: 记录全局最小差值和的容器
def getMaxCountMinSum(segment, index, abandon, total, minTotal):
    
    # 1. 递归终止条件：如果下标已经走到或超过了差值数组末尾
    if index >= len(segment):
        # 如果当前这一条路径算出来的总差值，比之前记录的最小值还要小
        if total < minTotal[0]:
            # 更新最小值（minTotal 是列表，通过 [0] 实现跨函数修改变量）
            minTotal[0] = total
        # 结束当前递归分支
        return

    # 2. 决策分支 A: 偶数对, 两两配对: 选择当前这对队伍进行匹配
    # 既然选了 index 和 index+1 组队，那么 index+1 就不能再跟后面组队了
    # 所以下标直接 +2, 跳到下下一对可能性去, 同时累加当前的差距值 segment[index]
    getMaxCountMinSum(segment, index + 2, abandon, total + segment[index], minTotal)

    # 3. 决策分支 B: 尝试跳过当前这个队伍（让他落单）
    # 条件：必须还没舍弃过队伍（!abandon），且当前分段的总人数是奇数
    # 说明: len(segment) 是差值数, 若差值数为偶数，代表总队伍数是奇数（如 3 队产生 2 个差）
    # 为了保证“匹配数最大”，奇数个队伍时必须舍弃一个，偶数个则一个都不能舍弃
    if not abandon and len(segment) % 2 == 0:  # 没有放放弃过且队伍个数是奇数
        # 标记 abandon 为 True，表示名额已用；下标只 +1，去看“后一个”与“后后一个”组队的可能
        # 因为这步是舍弃，所以 total 不变（没有产生新的匹配差距）
        getMaxCountMinSum(segment, index + 1, True, total, minTotal) 


# 算法入口
def getResult(n, d, arr):
    """
    :param n: 队伍个数n
    :param d: 允许的最大实力差距d
    :param arr: n个队伍的实力值数组
    :return: 匹配队伍最多的情况下匹配出的各组实力差距的总和最小
    """

    # 实力数组升序
    arr.sort()

    # ans记录各组实力差之和
    ans = 0

    # 此flag标记是否没有队伍可以匹配, true表示没有队伍可以匹配, 此时应该返回-1
    flag = True

    # segment用于保存分段, 差值
    segment = []
    for i in range(1, n):
        # 相邻两队的实力差diff
        diff = arr[i] - arr[i - 1]

        # 如果diff大于d，那么说明 i - 1 无法和 i 组队匹配
        if diff > d:
            # 此时分段开始
            if len(segment) > 0:
                flag = False
                minTotal = [float('inf')]
                getMaxCountMinSum(segment, 0, False, 0, minTotal)  # 计算分段部分的组队匹配的：匹配队伍最多的情况下匹配出的各组实力差距的最小总和
                ans += minTotal[0]
                segment.clear()  # 开始记录新的分段
        else:
            # 如果diff不大于d，那么说明 i - 1 可以和 i 组队匹配，此时将实力差（相当于一个组队匹配）计入分段
            segment.append(diff)

    # 最后一个分段也要记得处理，上面逻辑无法将最后一个分段处理到
    if len(segment) > 0:
        flag = False
        minTotal = [float('inf')]
        getMaxCountMinSum(segment, 0, False, 0, minTotal)
        ans += minTotal[0]

    if flag:
        return -1

    return ans


# 算法调用
print(getResult(n, d, arr))