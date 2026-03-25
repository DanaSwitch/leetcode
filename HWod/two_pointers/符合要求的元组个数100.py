import sys

# 双指针法解决 2-Sum
def two_sum_solve(nums, target, start_idx):
    l, r = start_idx, len(nums) - 1
    count = 0
    while l < r:
        s = nums[l] + nums[r]
        if s == target:
            count += 1
            lv, rv = nums[l], nums[r]
            while l < r and nums[l] == lv: l += 1
            while l < r and nums[r] == rv: r -= 1
        elif s < target: l += 1
        else: r -= 1
    return count

# 递归解决 K-Sum
def solve(nums, k, target, start_idx):
    if k == 2:
        return two_sum_solve(nums, target, start_idx)
    
    count = 0
    n = len(nums)
    for i in range(start_idx, n - k + 1):
        if i > start_idx and nums[i] == nums[i-1]: continue
        
        # 强力剪枝: 题目要求 2 <= k <= 100, n <= 200
        if sum(nums[i:i+k]) > target: break
        if nums[i] + sum(nums[n-k+1:n]) < target: continue
        
        count += solve(nums, k - 1, target - nums[i], i + 1)
    return count

def main():
    # 读取所有输入
    data = sys.stdin.read().split()
    if len(data) < 3: return
    
    # 星号解包: nums 拿走前面所有, k 和 target 拿走最后两个
    *nums_raw, k_raw, target_raw = data
    
    # 转换类型并排序（排序是去重和双指针的前提）
    nums = sorted(map(int, nums_raw))
    k = int(k_raw)
    target = int(target_raw)
    
    # 输出结果
    print(solve(nums, k, target, 0))

if __name__ == "__main__":
    main()