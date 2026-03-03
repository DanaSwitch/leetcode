import sys

def min_stones_to_half(n, weights):
    total_weight = sum(weights)

    if total_weight % 2 != 0:  # 不能均分
        print(-1)
        return

    target = total_weight // 2
    dp = [n] * (target + 1)  # dp[j] 表示要达到重量 j 至少需要多少石头
    dp[0] = 0  # 目标重量为 0 时，不需要取出雨花石

    for weight in weights:
        for j in range(target, weight - 1, -1):  # 倒序
            dp[j] = min(dp[j], dp[j - weight] + 1)  # 拿不拿石头, 拿的话重量减少weight, 石头数量减一 

    print(-1 if dp[target] == n else dp[target])  # dp[target] == n 表示怎么也凑不齐这个重量为 target 的石头


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())  # 读取雨花石个数
    weights = list(map(int, sys.stdin.readline().strip().split()))  # 读取雨花石重量
    min_stones_to_half(n, weights)