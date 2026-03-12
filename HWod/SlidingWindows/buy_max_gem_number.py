import sys

data = sys.stdin.read().split()
n = int(data[0])  # 宝石数量
lines = list(map(int, data[1:n+1]))
money = int(data[n+1])

left = 0
count = 0  # 宝石数量
window = 0

# 遍历右指针, 收缩左边界
for right in range(n):
    window += lines[right]
    while window > money and left <= right:
        window -= lines[left]
        left += 1
    count = max(count, right-left+1)
print(count)