cost = list(map(int, input().split()))
days = list(map(int, input().split()))

days = set(days)
max_days = max(days)

dp = [0] * (max_days+1)  # dp[i]表示到第i天的最低费用

for i in range(max_days+1):
    if i not in days:
        dp[i] = dp[i-1]  # 不玩就不花费
    else:
        # i最小是0, 记得max
        dp[i] = min(
            dp[max(0, i-1)] + cost[0],  # 一日票
            dp[max(0, i-3)] + cost[1],  # 三日票
            dp[max(0, i-7)] + cost[2],  # 一周票
            dp[max(0, i-30)] + cost[3]  # 一月票
        )

print(dp[max_days])