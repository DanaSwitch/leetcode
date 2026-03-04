# 处理输入
goodsNumber = int(input())  # 商品数量
days = int(input())  # 售货天数

goods_max_number = list(map(int, input().split()))  # 每件商品最大持有数量

prices = [list(map(int, input().split())) for _ in range(goodsNumber)]  # 商品价格列表

# 贪心算法
maxProfit = 0
for i in range(goodsNumber):  # 遍历每件商品
    for j in range(1, days):  # 遍历商品价格列表，求出每天的利润
        # 当前价格减去前一天价格，如果为负数则代表亏本，不计入利润       
        profit = max(0, prices[i][j] - prices[i][j - 1])
        maxProfit += profit * goods_max_number[i]  # 求出当前商品能够获取的最大利润

print(maxProfit)  # 输出最大利润