def my_sort(arr):
    n = len(arr)
    for i in range(n):
        # 字符串比较: 从左往右依次比较字符
        for j in range(i+1, n):
            if arr[i] + arr[j] > arr[j] + arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr  # 小的在前面

def solve():
    nums = input().split()

    # 情况一: 所有字符串都以 '0' 开头
    if all(s[0] == '0' for s in nums):
        result = ''.join(my_sort(nums[:]))
        print(result.lstrip('0') or '0')
        return

    # 情况二: 枚举不以 '0' 开头的字符串作为首元素
    best = None
    for i, s in enumerate(nums):
        if s[0] == '0':
            continue
        rest = []
        for j in range(len(nums)):
            if j != i:  # 选出s外的数字
                rest.append(nums[j])
        rest = my_sort(rest)  # 排序, 小的在前面
        candidate = s + ''.join(rest)  # 拼接
        if best is None or candidate < best:
            best = candidate

    print(best)

solve()