import sys
nums = list(map(int, input().strip().split()))
k = int(input())
target = int(input())
n = len(nums)
nums.sort()


# 两数之和(去重)
def two_sum(left, right, t):
    count = 0
    while left < right:
        cur_sum = nums[left] + nums[right]
        if cur_sum == t:
            count += 1
            while left < right and nums[left] == nums[left+1]:
                left += 1
            while left < right and nums[right] == nums[right-1]:
                right -= 1
            left += 1
            right -= 1
        
        elif cur_sum < t:
            left += 1
        else:
            right -= 1
    return count

def k_sum_count(start, remaining, t):
    # 先固定一个数, 从剩下的数组里面选k-1个数, 使得和为targrt - 固定值
    count = 0
    if remaining == 2:
        return two_sum(start, n-1, t)  # 从start开始
    for i in range(start, n - remaining + 1):
        if i > start and nums[i] == nums[i-1]:  # 注意这里是i-1
            continue
        count += k_sum_count(i+1, remaining-1, t-nums[i])
    return count

print(k_sum_count(0, k, target))
