"""
思想: 撞边界  计算新坐标后立即判断
     撞身体（普通移动）移除尾巴之后判断
     撞身体（吃食物增长）加入新头之前判断
"""
from collections import deque

def solve():
    ops = input().split()            # 读取操作序列
    N, M = map(int, input().split()) # 行, 列

    grid = []
    start = None
    for i in range(N):
        row = input().split()
        grid.append(row)
        for j in range(M):
            if row[j] == 'H':
                start = (i, j)      # 记录蛇头初始位置
                grid[i][j] = 'E'   # 起始格视为空格，方便后续统一处理

    # 用双端队列表示蛇身，队头 = 蛇头，队尾 = 尾巴
    body = deque([start])
    body_set = set([start])  # 集合用于 O(1) 判断碰撞

    # 四个方向的行列偏移量
    dr = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    direction = 'L'                 # 初始方向向左

    for op in ops:
        if op in ('U', 'D', 'L', 'R'):  # 上下左右
            direction = op          # 转向：只更新方向，蛇不移动
            continue

        # op == 'G'：按当前方向移动一格
        hr, hc = body[0]  # 当前蛇头坐标
        drow, dcol = dr[direction]
        nr, nc = hr + drow, hc + dcol    # 计算新蛇头坐标

        # 超出边界，游戏结束
        if nr < 0 or nr >= N or nc < 0 or nc >= M:
            break

        ate_food = (grid[nr][nc] == 'F')

        if ate_food:
            # 吃到食物：蛇身增长，新蛇头加入队头，尾巴不动
            grid[nr][nc] = 'E'          # 食物消耗掉
            if (nr, nc) in body_set:    # 新蛇头与身体重叠，碰撞结束
                body.appendleft((nr, nc))  # 加进去计算长度
                break
            body.appendleft((nr, nc))
            body_set.add((nr, nc))
        else:
            # 正常移动：先移除尾巴，再判断碰撞
            tail = body.pop()
            body_set.remove(tail)
            if (nr, nc) in body_set:    # 与身体碰撞，游戏结束
                body.appendleft((nr, nc))  # 加进去计算长度
                break
            body.appendleft((nr, nc))
            body_set.add((nr, nc))

    print(len(body))    # 输出游戏结束或操作完成时的蛇长

solve()