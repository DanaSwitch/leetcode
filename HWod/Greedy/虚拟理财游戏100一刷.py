m, N, X = map(int, input().split())  # 产品数, 总投资数, 风险数
rates  = list(map(int, input().split()))
risks  = list(map(int, input().split()))
max_inv = list(map(int, input().split()))

best = 0  # 最大回报
result = [0] * m

# 单产品投资
for i in range(m):
    if risks[i] <= X:
        inv = min(max_inv[i], N)
        profit = inv * rates[i]
        if profit > best:
            best = profit
            result = [0] * m  # 重置投资组合
            result[i] = inv

# 双产品投资：枚举所有组合
for i in range(m):
    for j in range(i + 1, m):
        if risks[i] + risks[j] <= X:
            # 贪心: 优先把钱投给回报率更高的
            high, low = (i, j) if rates[i] >= rates[j] else (j, i)
            inv_hi = min(max_inv[high], N)  # 先满足回报高的
            inv_lo = min(max_inv[low], N - inv_hi)  # 剩下的给回报低的
            profit = inv_hi * rates[high] + inv_lo * rates[low]
            if profit > best:
                best = profit
                result = [0] * m   # 重置投资组合
                result[high] = inv_hi
                result[low] = inv_lo

print(*result)