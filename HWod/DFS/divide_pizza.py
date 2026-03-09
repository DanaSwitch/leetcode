import sys

def solve():
    lines = sys.stdin.read().strip().split()
    n = int(lines[0])
    nums = list(map(int, lines[1:]))
    nums = nums + nums  # 复制一份
    memo = {}
    def dfs(left, right, eating):
        # 递归出口: 返回0, 表示吃完了
        if left > right:
            return 0        
        if (left, right, eating)  in memo:
            return memo[(left, right, eating)]        
        # 吃货选
        if eating == True: 
            eating_left = nums[left] + dfs(left+1, right, False)
            eating_right = nums[right] + dfs(left, right-1, False)
            res = max(eating_left, eating_right)
        # 馋嘴选
        else:
            if nums[left] > nums[right]:
                res = dfs(left+1, right, True)
            else:
                res = dfs(left, right-1, True)
        memo[(left, right, eating)] = res
        return res
    max_sum = 0  # 初始化为0
    # 遍历从哪一块开始吃
    for i in range(n):
        # 吃货吃第一块，第二块给馋嘴
        # (i+1, i+n-1) 固定了长为 n 的区间
        ans = nums[i] + dfs(i+1, i+n-1, False)  # ans在每次循环都会更新
        max_sum = max(max_sum ,ans)  # 记录最大的总和
    print(max_sum)


if __name__ == "__main__":
    solve()