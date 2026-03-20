"""
注意排序规则写 key=lambda, 而不是k

输入
[1,10],[15,20],[18,30],[33,40]
[5,4,3,2]
输出
1
说明
合并后：[1,10], [15,30], [33,40], 使用5, 3两个连接器连接后只剩下[1,40]。
"""
import re

def merge(segs):
    sort_segs = sorted(segs, key=lambda x: x[0])
    result = [sort_segs[0]]
    for i in range(1, len(sort_segs)):
        last = result[-1]
        start, end = sort_segs[i]
        if start <= last[1]:
            last[1] = max(last[1], end)
        else:
            result.append(sort_segs[i])
    return result

input1 = input().strip()  # 区间
input2 = input().strip()  # 连接器

nums = list(map(int, re.findall(r'\d+', input1)))
ans = [[nums[i], nums[i+1]] for i in range(0, len(nums), 2)]
joinArr = list(map(int, re.findall(r'\d+', input2)))

# 合并区间
merged = merge(ans)

dist = []
# 计算相邻区间间隙
for i in range(1, len(merged)):
    tmp = merged[i][0] - merged[i-1][1]
    dist.append(tmp)

dist.sort(reverse=True)
joinArr.sort(reverse=True)

count = 0  # 合并区间数
i = j = 0
while i < len(dist) and j < len(joinArr):
    if dist[i] <= joinArr[j]:
        count += 1
        i += 1
        j += 1
    else:
        i += 1 # 找更小的差异
print(len(dist) + 1 - count)