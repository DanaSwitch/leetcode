nums = list(map(int, input().strip().split()))
n = len(nums)
half = n // 2
total = sum(nums)
min_diff = [float('inf')]  # 最小差异

def dfs(index, count, cur_sum):  # count: 选了count个数
    if count == 0:
        diff = abs(total - cur_sum*2)  # 当前递归的差异
        min_diff[0] = min(min_diff[0], diff)
        return

    if index > n:
        return
    
    leafting = n - index
    if leafting < count:
        return
    
    # 选
    dfs(index+1, count-1, cur_sum+nums[index])
    # 不选
    dfs(index+1, count, cur_sum)

dfs(0, half, 0)
print(min_diff[0])