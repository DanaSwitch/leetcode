import sys

# 输入获取
n, m = map(int, input().split())  # 矩阵 [行数, 列数]
matrix = [list(map(int, input().split())) for _ in range(n)]  # 矩阵
k = int(input())  # 目标数组长度
nums = list(map(int, input().split()))  # 目标数组

# cnts[num] 记录的是 目标数组中num元素的个数
cnts = [0] * 1000
for num in nums:
    cnts[num] += 1


# 算法入口
def getResult():
    # 未完成匹配的元素的个数, k是目标数组长度
    total = k

    # 记录最小子矩阵的宽度
    minLen = float('inf')  # 代表正无穷大

    l = 0  # 当前子矩阵的左边界（列号）
    r = 0  # 当前子矩阵的右边界（列号）

    # 如果右边界未越界，则可以继续尝试找最小子矩阵
    while r < m:
        # 将第r列所有元素纳入子矩阵, 判断这列是否有需要的数据
        for i in range(n):
            #  第r列的元素numR
            numR = matrix[i][r]

            # cnts[numR] 记录的是 目标数组中numR元素的个数，也可以理解为：目标数组中numR元素剩余未匹配的个数
            # 如果numR是目标数组元素，则cnts[numR]初始时必然大于0，且随着子矩阵扩大范围
            # 如果子矩阵中包含numR元素个数超过了初始cnts[numR]数量，则超出部分起不到匹配效果，即不能影响总的未匹配数量
            if cnts[numR] > 0:
                total -= 1
            cnts[numR] -= 1

        # 纳入r列后，看看总的未匹配元素数量total还有几个，如果total为0，则说明当前子矩阵匹配到了所有目标数组元素
        while total == 0:
            # 若此时子矩阵宽度 r - l + 1 更小，则更新最小子矩阵宽度
            minLen = min(minLen, r - l + 1)

            # 由于当前子矩阵已经匹配到所有目标数组元素，因此下一步应该将 l 右移，尝试更小宽度的子矩阵
            for i in range(n):
                # l 右移，相当于当前子矩阵移除了第 l 列所有元素，被移除的元素numL如果是目标数组元素，则对应的未匹配数量应该被恢复
                numL = matrix[i][l]

                # 如果当前numL不是目标数组元素，或者当前numL是目标数组元素，但是属于超出部分（这两种情况必然cnts[numL] < 0），则对应numL元素的恢复，不能影响到整体未匹配数量total，
                # 如果当前numL是目标数组元素，且不是超出部分（此时必然cnts[numL] >= 0），则对应numL元素的恢复，会影响到整体未匹配数量total
                if cnts[numL] >= 0:
                    total += 1
                cnts[numL] += 1

            # l右移，且下一轮要继续检查l右移后的子矩阵是否依旧能覆盖目标数组所有元素
            l += 1

        # r右移
        r += 1

    if minLen == float('inf'):
        return -1
    else:
        return minLen


# 算法调用
print(getResult())