import sys

n = int(sys.stdin.readline().strip())
points = set()
point_list = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().strip().split())
    point = (x, y)
    points.add(point)
    point_list.append(point)

square_count = 0

for i in range(n):
    x1, y1 = point_list[i]
    for j in range(i + 1, n):
        x2, y2 = point_list[j]

        # 边向量: (dx, dy) = (x2-x1, y2-y1)
        # -----------------------------------------------
        # 方向一: 将边向量顺时针旋转90° → 新向量 (-dy, dx)
        #         即 (-(y2-y1), x2-x1) = (y1-y2, x2-x1)
        #
        #   P1 ——————→ P2          旋转向量方向(向下)
        #   |          |           ↓
        #   p3 ————— p4
        #
        # p3 = P1 + 旋转向量 = (x1+(y1-y2), y1+(x2-x1))
        #                    = (x1-(y2-y1), y1+(x1-x2))   ← 提负号
        # p4 = P2 + 旋转向量 = (x2+(y1-y2), y2+(x1-x2))
        # -----------------------------------------------
        p3 = (x1 - (y2 - y1), y1 + (x1 - x2))
        p4 = (x2 - (y2 - y1), y2 + (x1 - x2))

        if p3 in points and p4 in points:
            square_count += 1

        # -----------------------------------------------
        # 方向二: 将边向量逆时针旋转90° → 新向量 (dy, -dx)
        #         即 (y2-y1, -(x2-x1)) = (y2-y1, x1-x2)
        #
        #   p5 ————— p6
        #   |          |           旋转向量方向(向上)
        #   P1 ——————→ P2          ↑
        #
        # p5 = P1 + 旋转向量 = (x1+(y2-y1), y1+(x1-x2))
        #                    = (x1-(y1-y2), y1-(x2-x1))   ← 提负号
        # p6 = P2 + 旋转向量 = (x2+(y2-y1), y2+(x1-x2))
        # -----------------------------------------------
        p5 = (x1 - (y1 - y2), y1 - (x2 - x1))
        p6 = (x2 - (y1 - y2), y2 - (x2 - x1))

        if p5 in points and p6 in points:
            square_count += 1

# 每条边 (i,j) 只枚举一次，但一个正方形有4条边
# 每个正方形恰好被累计4次，除以4得真实数量
print(square_count // 4)