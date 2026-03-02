# 输入获取
A, B = input().strip().split()
m, n = len(B), len(A)  # m是行, n是列


# 算法入口
def getResult():
    # 初始时preRow记录第一行上各点到(0,0)点的最短距离，即为(0,0) -> (0,j) 的直线路径
    preRow = [i for i in range(n + 1)]  # 上一行

    # 初始时curRow记录第二行上各点到(0,0)点的最短距离
    curRow = [0] * (n + 1)  # 当前行

    for i in range(1, m + 1):  # 遍历每一行
        # curRow[0]是指 (i, 0)点 到 (0,0)点 的最短距离，即为(0,0) -> (i, 0) 的直线路径
        curRow[0] = i

        for j in range(1, n + 1):
            if A[j - 1] == B[i - 1]:
                # 如果可以走斜线，则选走斜线的点
                curRow[j] = preRow[j - 1] + 1
            else:
                # 如果不能走斜线，则从当前点的上方点、左方点中选择一个较小值
                # preRow表示上一行, j是当前遍历的点
                curRow[j] = min(preRow[j], curRow[j - 1]) + 1

        preRow = curRow[:]  # 把 curRow 此时此刻的所有值, 复制给 preRow

    return curRow[n]


# 算法调用
print(getResult())