import sys
import math

# 判断T时刻能否完成
def check(time, defaultCnt, extraCnt, nums):
    max_time = 0
    for i in range(len(nums)):
        if nums[i] > defaultCnt * time:
            extra = nums[i] - defaultCnt * time
            need_time = math.ceil(extra / extraCnt)
            max_time += need_time
    return max_time <= time
    

def solve():
    lines = sys.stdin.readline().split()
    if not lines:
        return
    n, defaultCnt, extraCnt = int(lines[0]), int(lines[1]), int(lines[2])
    nums = list(map(int, sys.stdin.readline().strip().split()))

    left, right = 0, max(nums)
    total_time = 0  # 全部时间
    while left <= right:
        mid = (left + right) // 2
        if check(mid, defaultCnt, extraCnt, nums):
            total_time = mid
            right = mid - 1
        else:
            left = mid + 1
    return total_time

if __name__ == "__main__":
    print(solve())