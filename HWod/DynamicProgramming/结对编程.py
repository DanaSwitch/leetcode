"""
暴力解:
对于每个中间元素 j, 统计:
左边比 level[j] 小的数量 left_less
左边比 level[j] 大的数量 left_greater
右边比 level[j] 小的数量 right_less
右边比 level[j] 大的数量 right_greater
则以 j 为中间元素的组合数 = left_less * right_greater + left_greater * right_less
"""
n = int(input())
level = list(map(int, input().split()))

result = 0

for j in range(1, n - 1):
    left_less = left_greater = 0
    for i in range(j):
        if level[i] < level[j]:
            left_less += 1
        elif level[i] > level[j]:
            left_greater += 1
    
    right_less = right_greater = 0
    for k in range(j + 1, n):
        if level[k] < level[j]:
            right_less += 1
        elif level[k] > level[j]:
            right_greater += 1
    
    result += left_less * right_greater + left_greater * right_less

print(result)

"""
# 树状数组更新
def update(tree, index, delta):
    n = len(tree) - 1
    while index <= n:
        tree[index] += delta
        index += index & -index

# 树状数组查询前缀和
def query(tree, index):
    res = 0
    while index > 0:
        res += tree[index]
        index -= index & -index
    return res

n = int(input())
nums = list(map(int, input().split()))
maxv = max(nums)

tri1 = [0] * (maxv + 1)
tri2 = [0] * (maxv + 1)

# tri2 放所有元素
for x in nums:
    update(tri2, x, 1)

ans = 0
for num in nums:
    # 从右侧移除
    update(tri2, num, -1)

    leftLess = query(tri1, num - 1)
    leftMore = query(tri1, maxv) - query(tri1, num)
    rightLess = query(tri2, num - 1)
    rightMore = query(tri2, maxv) - query(tri2, num)

    ans += leftLess * rightMore + leftMore * rightLess
    # 加入左侧
    update(tri1, num, 1)

print(ans)
"""