import sys
input = sys.stdin.readline

def solve():
    n = int(input())  # 操作数量

    # 偏移量 offset=100, 坐标 x -> x+100
    SIZE = 200
    OFFSET = 100
    # bytearray  ≈  C 的 unsigned char 数组 + 安全检查
    grid = bytearray(SIZE * SIZE)  # 一维展开, 初始化为0, 访问更快

    for _ in range(n):
        parts = input().split()
        op = parts[0]
        x1 = int(parts[1]) + OFFSET
        y1 = int(parts[2]) + OFFSET
        x2 = int(parts[3]) + OFFSET
        y2 = int(parts[4]) + OFFSET

        x_min, x_max = min(x1, x2), max(x1, x2)
        y_min, y_max = min(y1, y2), max(y1, y2)
        
        val = 1 if op == 'd' else 0
        
        for x in range(x_min, x_max):
            base = x * SIZE  # 二维转一维
            for y in range(y_min, y_max):
                grid[base + y] = val
    
    print(sum(grid))

solve()