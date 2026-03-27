# 0/1 背包问题
import sys

# 均分一半重量需要的最少雨花石数目
def get_half_stones(n, stones):
    total_weights = sum(stones)  # 总的重量
    if total_weights % 2 == 1:  # 奇数不能均分
        print(-1)
        return
    
    target = total_weights // 2  # 均分重量
    # dp[i] 表示达到重量i至少需要的石头数
    dp = [n+1] * (target+1)  # n+1 是不可能达到的数
    dp[0] = 0
    for stone in stones:
        for i in range(target, stone - 1, -1):
            dp[i] = min(dp[i], dp[i-stone]+1)
    print(dp[target] if dp[target] < n else -1)


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())  # 石头数
    stones = list(map(int, sys.stdin.readline().strip().split()))
    get_half_stones(n, stones)