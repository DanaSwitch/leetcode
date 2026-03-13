"""
思路: 也就是说, 最后一辆车到达的时间, 是所有车自由到达时间的最大值
      自由到达时间 = 出发时刻 + 不受阻挡跑完全程的时间
"""
M, N = map(int, input().split())  # 车辆数, 总路程

max_arrive = 0
for i in range(M):
    speed = float(input())
    arrive = i + (N/speed)  # 第 i 辆车的自由到达时刻
    max_arrive = max(max_arrive, arrive)

travel_time = round(max_arrive - (M - 1), 3)  # 减去出发时间, 保留三位小数
print(f"{travel_time:.3f}".rstrip("0").rstrip("."))  # 去掉多余的0