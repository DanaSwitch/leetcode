import sys

line = sys.stdin.readline().strip()
# 去掉开头结尾的中括号
line = line[1:-1]
books = []
for pair_str in line.split('],['):
    pair_str = pair_str.strip('[]')  # 移除多余括号, 有[ 和 ]其中一个就可以去除
    a, b = map(int, pair_str.split(','))
    books.append([a, b])


# 二分查找
def binarySearch(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) >> 1

        if key > arr[mid]:
            low = mid + 1
        elif key < arr[mid]:
            high = mid - 1
        else:
            return mid

    return -(low + 1)


# 最长递增子序列
def getMaxLIS(nums):
    # dp数组元素dp[i]含义是：长度为i+1的最优子序列的尾数
    dp = [nums[0]]

    for i in range(1, len(nums)):
        if nums[i] > dp[-1]:
            dp.append(nums[i])
            continue

        if nums[i] < dp[0]:
            dp[0] = nums[i]
            continue

        idx = binarySearch(dp, nums[i])
        if idx < 0:
            dp[-idx - 1] = nums[i]

    return len(dp)


# 算法入口
def handle(books):
    # 长度升序，若长度相同，则宽度降序
    books.sort(key=lambda x: (x[0], -x[1]))
    widths = list(map(lambda x: x[1], books))
    return getMaxLIS(widths)


# 算法调用
print(handle(books))