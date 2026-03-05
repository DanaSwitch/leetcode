import sys

def solve(n, t, k, sports):
    # dp[i][j]表示用i个运动凑成卡路里j的总方法数
    dp = [[0] * (t+1) for _ in range(k+1)]  # t是列, k是行
    dp[0][0] = 1
    # 遍历每一个运动项目, 每个运动只能用一次
    for sport in sports:
        # 倒序遍历运动个数
        for i in range(k, 0, -1):
            # 倒序遍历卡路里数
            for j in range(t, sport-1, -1):
                # 选不选都加起来
                dp[i][j] += dp[i-1][j-sport]
    print(dp[k][t])


if __name__ == "__main__":
    line = sys.stdin.readline().split()
    n, t, k = map(int, line)
    sports = list(map(int, sys.stdin.readline().strip().split()))
    solve(n, t, k, sports)