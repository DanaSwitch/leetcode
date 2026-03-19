import heapq

def main():
    T, N = map(int, input().split())
    times = list(map(int, input().split()))
    total_travel_time = sum(times)
    # 记录城市的信息
    city_info = []
    for _ in range(N):
        M, D = map(int, input().split())
        city_info.append((M, D))
    # 演出可以使用的天数    
    remaining_day = T - total_travel_time

    # 取负数实现大顶堆
    pq = []
    for i, (M, _) in enumerate(city_info):
        heapq.heappush(pq, (-M, i))

    res = 0
    # 贪心选择收入高的城市进行演出
    while remaining_day > 0:
        income, idx = heapq.heappop(pq)
        income = -income
        res += income
        # 更新该城市下一天收入确保不小于0，并重新入队
        new_income = max(0, income - city_info[idx][1])
        heapq.heappush(pq, (-new_income, idx))
        remaining_day -= 1

    print(res)

if __name__ == "__main__":
    main()
