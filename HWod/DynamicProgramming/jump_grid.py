def solve(nums):
    if not nums:
        return 0
    n = len(nums)
    dp = [0]*(n+1)

    dp[0] = 0
    dp[1] = nums[0]  # dp[i]表示从前i个格子中取的最大值

    for i in range(2, n+1):
        dp[i] = max(dp[i-1], dp[i-2]+nums[i-1])
    return dp[n]

if __name__ == "__main__":
    nums = list(map(int, input().split()))
    if len(nums) == 1:
        result = nums[0]
    else:
        result = max(solve(nums[2:-1])+nums[0], solve(nums[1:]))
    print(result)