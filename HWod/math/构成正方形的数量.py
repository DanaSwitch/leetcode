import sys

# 读取输入
n = int(sys.stdin.readline().strip())
points = set()
point_list = []

# 读取坐标并存入集合和列表
for _ in range(n):
    x, y = map(int, sys.stdin.readline().strip().split())
    point = (x, y)
    points.add(point)
    point_list.append(point)

square_count = 0

# 遍历所有点对，检查是否能构成正方形
for i in range(n):
    x1, y1 = point_list[i]

    for j in range(i + 1, n):
        x2, y2 = point_list[j]

        # 计算两个可能的对角点
        p3 = (x1 - (y1 - y2), y1 + (x1 - x2))
        p4 = (x2 - (y1 - y2), y2 + (x1 - x2))

        if p3 in points and p4 in points:
            square_count += 1

        # 计算另外两个可能的对角点
        p5 = (x1 + (y1 - y2), y1 - (x1 - x2))
        p6 = (x2 + (y1 - y2), y2 - (x1 - x2))

        if p5 in points and p6 in points:
            square_count += 1

# 每个正方形被计算了4次，因此结果需要除以4
print(square_count // 4)