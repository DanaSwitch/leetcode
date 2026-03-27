# 判断 0-n 中满足条件的数
def solve(n):
    if n < 0: return 0
    s = bin(n)[2:]  # 转为二进制
    memo = {}

    def dp(index, last1, last2, is_limit, is_started):
        # 定义状态元组作为 memo 的 key
        state = (index, last1, last2, is_limit, is_started)
        # 遍历到最后一位
        if index == len(s):
            return 1       
        if state in memo:
            return memo[state]
        res = 0
        upper = int(s[index]) if is_limit else 1  # 当前位能够填的最大数字
        # 遍历每个数字可以选的数
        for digit in range(upper + 1):
            # 检查是否非法：前前一位是1，前一位是0，当前位填1
            if is_started and last2 == 1 and last1 == 0 and digit == 1:
                continue           
            res += dp(
                index + 1, 
                digit, 
                last1, 
                is_limit and (digit == upper),   #  前面数字是否压着边界走的
                is_started or (digit == 1)  # 填过数字就一直是True
            )           
        memo[state] = res
        return res

    return dp(0, 0, 0, True, False)  # is_limit 一开始就是True

# 主程序
# 例如输入：1 10
l, r = map(int, input().split())
print(solve(r) - solve(l - 1))