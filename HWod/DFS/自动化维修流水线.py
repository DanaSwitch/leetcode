import sys
sys.setrecursionlimit(10**7)

# 递归回溯尝试分配
def backtrack(task, buckets, idx, limit):
    if idx == len(task):
        return True

    cur = task[idx]

    for i in range(len(buckets)):
        # 剪枝：状态重合
        if i > 0 and buckets[i] == buckets[i - 1]:
            continue

        if buckets[i] + cur <= limit:
            buckets[i] += cur
            if backtrack(task, buckets, idx + 1, limit):
                return True
            buckets[i] -= cur

        # 剪枝：当前桶为空，后面不用再试
        if buckets[i] == 0:
            break
    return False


def check(task, m, limit):
    buckets = [0] * m
    return backtrack(task, buckets, 0, limit)


n, m = map(int, sys.stdin.readline().split())
task = list(map(int, sys.stdin.readline().split()))

task.sort(reverse=True)

l, r = task[0], sum(task)

# 二分
while l < r:
    mid = (l + r) // 2
    if check(task, m, mid):
        r = mid
    else:
        l = mid + 1

print(l)
