n = int(input())  # 区间数
nums = []

for _ in range(n):
    a, b = map(int, input().split())
    nums.append([a, b])

sort_nums = sorted(nums, key=lambda x: x[0])
common = []  # 公共区间

# 不断合并公共交集
for i in range(n):
    for j in range(i+1, n):
        start, end = sort_nums[i]
        s, e = sort_nums[j]
        low = max(start, s)
        high = min(end, e)
        if low <= high:  # 合并
            common.append([low, high])

sort_common = sorted(common, key=lambda x: x[0])

if not common:
    exit()  # 直接终止程序

# 合并
result = [sort_common[0]]  # 二维转为一维

for start, end in sort_common[1:]:
    s, e = result[-1]
    if start <= e:
        # 合并区间
        result[-1] = [s, max(end, e)]
    else:
        result.append([start, end])

for a, b in result:
    print(a, b)