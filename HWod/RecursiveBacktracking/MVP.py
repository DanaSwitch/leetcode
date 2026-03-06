import sys

# 提高递归深度限制
sys.setrecursionlimit(10000)

# 读取输入
t = int(input())
scores = list(map(int, input().split()))

total = sum(scores)
scores.sort(reverse=True)  # 降序排序是核心优化：先尝试大的数值

def can_partition(target):
    """
    检查能否将 scores 划分为若干组，每组和均为 target
    """
    if total % target != 0:
        return False
    
    k = total // target
    used = [False] * t  # 记录该分钟的分数是否已被分配
    
    def backtrack(k_idx, current_sum, start_idx):
        """
        k_idx: 当前正在凑第几个子集
        current_sum: 当前子集已有的分值和
        start_idx: 从哪个分数开始搜索，避免重复组合
        """
        # 如果已经成功凑齐了 k 个子集（其实凑齐 k-1 个，剩下的自然也齐了）
        if k_idx == k:
            return True
        
        # 当前子集已凑满，开始凑下一个子集
        if current_sum == target:
            # 填下一个桶时，重新从第一个分数开始找没用过的
            return backtrack(k_idx + 1, 0, 0)
        
        # 尝试选择一个分数放入当前子集
        for i in range(start_idx, t):
            # 剪枝：如果已被使用，或者加入后超过目标值，跳过
            if used[i] or current_sum + scores[i] > target:
                continue
            
            # 关键剪枝：如果当前分数和前一个分数相同，且前一个没被用过，
            # 说明前一个分数在这一层已经尝试失败了，直接跳过。
            if i > 0 and scores[i] == scores[i-1] and not used[i-1]:
                continue
            
            # 按照你要求的写法：标记 -> 递归 -> 回溯
            used[i] = True
            if backtrack(k_idx, current_sum + scores[i], i + 1):
                return True
            used[i] = False  # 回溯
            
            # 特殊剪枝：如果当前尝试是桶的开头或者是桶的结尾却失败了，
            # 那么这个分支一定无法完成划分，直接返回 False。
            if current_sum == 0 or current_sum + scores[i] == target:
                return False
                
        return False

    return backtrack(1, 0, 0)

# 从单分钟最大得分开始枚举目标值 S
for s in range(scores[0], total + 1):
    if total % s == 0:  # 只有能整除总分的 S 才需要尝试
        if can_partition(s):
            print(s)
            break