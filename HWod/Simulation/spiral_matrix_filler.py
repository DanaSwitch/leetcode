import math

def solve():
    # 读取输入 n(数字个数), m(行数)
    line = input().split()
    if not line: return
    n, m = map(int, line)

    # 1. 计算列数 c, 向上取整
    c = math.ceil(n / m)
    
    # 2. 初始化矩阵，填充为 '*'
    matrix = [['*' for _ in range(c)] for _ in range(m)]
    
    # 3. 定义螺旋移动的方向：右、下、左、上
    dx = [0, 1, 0, -1]  # 控制行
    dy = [1, 0, -1, 0]  # 控制列
    
    x, y, di = 0, 0, 0 # 初始位置 (0,0) 和 初始方向 (右)
    
    for i in range(1, n + 1):
        matrix[x][y] = str(i)
        
        # 尝试下一步
        next_x, next_y = x + dx[di], y + dy[di]
        
        # 检查是否需要转向: 越界 or 已经填过数字
        if not (0 <= next_x < m and 0 <= next_y < c and matrix[next_x][next_y] == '*'):
            di = (di + 1) % 4
            next_x, next_y = x + dx[di], y + dy[di]  # 转向
            
        x, y = next_x, next_y

    # 4. 按行打印矩阵
    for row in matrix:
        print(" ".join(row))

solve()