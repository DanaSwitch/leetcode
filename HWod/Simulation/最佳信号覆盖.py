def solve():
    N, D = map(int, input().split())  # AP数量N 和 最大覆盖距离D
    # 读取每个AP的位置和信号强度
    aps = [list(map(int, input().split())) for _ in range(N)]

    # 确定搜索范围: 最远只需搜到最大AP坐标+D
    max_x = max(ap[0] for ap in aps) + D
    max_y = max(ap[1] for ap in aps) + D
    
    best_signal = -1  # 当前最强信号
    best_pos = None   # 当前最优坐标
    
    # 遍历所有候选坐标(x,y都从1开始，因为题目要求x,y>0)
    for px in range(1, max_x + 1):
        for py in range(1, max_y + 1):
            # 计算这个点的总信号强度
            total_wifi = 0
            for (ax, ay, s) in aps:  # s是ap的信号强度
                # 切比雪夫距离
                d = max(abs(px - ax), abs(py - ay))
                # 只有距离<=D的AP才能覆盖到这个点
                if d <= D:
                    total_wifi += s // (1 + d)  # 向下取整
            
            # 更新最优解, 严格大于, 保证字典序最小
            if total_wifi > best_signal:
                best_signal = total_wifi
                best_pos = (px, py)
    
    print(best_pos[0], best_pos[1])

solve()