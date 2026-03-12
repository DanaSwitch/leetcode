import sys

# 不能排序, 顺序会乱

lines = list(map(int, sys.stdin.readline().strip().split(',')))
n = len(lines)
left, right = 0, n-1
area = min(lines[left], lines[right]) * (n-1)  # 初始化面积

def update_area(left, right):
    return min(lines[left], lines[right]) * (right - left)

while left < right:
    if lines[left] < lines[right]:
        # 让矮的移动
        left += 1
        cur_area = update_area(left, right)
        area = max(cur_area, area)
    else:
        right -= 1
        cur_area = update_area(left, right)
        area = max(cur_area, area)

print(area)