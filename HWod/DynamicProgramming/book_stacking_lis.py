# 输入获取
books = eval(input())


# 二分查找
def binarySearch(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) >> 1
        midVal = arr[mid]

        if key > midVal:
            low = mid + 1
        elif key < midVal:
            high = mid - 1
        else:
            return mid

    return -(low + 1)


# 最长递增子序列
def getMaxLIS(nums):
    # dp数组元素dp[i]含义是：长度为i+1的最优子序列的尾数
    dp = [nums[0]]

    for i in range(1, len(nums)):
        # 大于最后一个: 宽度大于最大的, 就加入末尾
        if nums[i] > dp[-1]:
            dp.append(nums[i])
            continue
        # 小于第一个: 更新起点
        if nums[i] < dp[0]:
            dp[0] = nums[i]
            continue
        # 在中间: 用二分查找找到应该插入的位置
        idx = binarySearch(dp, nums[i])
        # 在中间相等则什么都不做, 否则替换掉第一个比它大的数
        if idx < 0:
            dp[-idx - 1] = nums[i]

    return len(dp)


# 算法入口
def getResult(books):
    # 长度升序，若长度相同，则宽度降序
    books.sort(key=lambda x: (x[0], -x[1]))
    widths = list(map(lambda x: x[1], books))
    return getMaxLIS(widths)


# 算法调用
print(getResult(books))