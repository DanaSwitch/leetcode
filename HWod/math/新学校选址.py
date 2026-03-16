import sys

n = sys.stdin.readline().strip()
n = int(n)

nums = list(map(int, sys.stdin.readline().strip().split()))

nums.sort()

# 中位数是最小的

if n % 2 == 1:
    print(nums[n//2])
else:
    print(nums[n//2 - 1])