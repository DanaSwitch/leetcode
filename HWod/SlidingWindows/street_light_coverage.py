# 输入获取
n = int(input())
arr = list(map(int, input().split()))


# 算法入口
def getResult():
    rans = []

    for i in range(n):
        center = i * 100
        rans.append([center - arr[i], center + arr[i]])

    # 按起始位置升序，起始位置相同，则继续按结束位置降序
    rans.sort(key=lambda ran: (ran[0], -ran[1]))

    ans = 0

    t = rans[0][1]  # 上一个区间的结束位置, 初始化为第一个区间的右边
    for i in range(1, n):
        start, end = rans[i]  # 当前区间的【开始位置，结束位置】

        # 有交集, 就合并
        if t >= start:
            # 合并后的新区间将变为下一轮的上一个区间，t为新区间的结束位置
            t = max(end, t)
        else:
            # 没有交集，则统计区间间隙 s - t
            ans += start - t
            #  当前区间变为下一轮的上一个区间，更新t
            t = end  # t更新为上一个区间的末尾

    return ans


# 算法调用
print(getResult())