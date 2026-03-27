import sys

# 判断距离为 d 时能种的树
def check(d, nums, tree_total):
    count = 1
    last_tree = nums[0]
    for i in range(1, len(nums)):
        if nums[i] - last_tree >= d:
            count += 1
            last_tree = nums[i]
    return count >= tree_total

def solve():
    line1 = sys.stdin.readline()
    if not line1: return
    n = int(line1.strip())
    nums = sorted(list(map(int, sys.stdin.readline().strip().split())))
    tree_total = int(sys.stdin.readline().strip())

    # 二分查找
    low = 1
    high = nums[-1] - nums[0]
    ans = 0  # 种树间隔
    while low <= high:
        mid = (low + high) // 2
        if check(mid, nums, tree_total):
            ans = mid      # 记录当前可行的最大间隔
            low = mid + 1  # 尝试更大的间隔
        else:
            high = mid - 1 # 间隔太大了，缩减范围       
    print(ans)

solve()