from collections import Counter

nums = list(map(int, input().strip().split(',')))
n = int(input())

count = Counter(nums)

max_count = max(count.values())  # 最多数的数量
max_sum = 0  # 最多数的种类
for i in count.values():
    if i == max_count:
        max_sum += 1

print(max(len(nums), (n+1)*(max_count-1)+max_sum))