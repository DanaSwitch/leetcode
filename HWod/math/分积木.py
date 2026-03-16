import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().strip().split()))

total_xor = 0  # 异或和

for w in nums:
    total_xor ^= w

if total_xor != 0:
    print("NO")
else:
    min_num = min(nums)
    print(sum(nums) - min_num)