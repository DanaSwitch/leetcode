import sys

def solve():
    # 1. 使用 sys.stdin.read() 一次性读取所有输入内容
    # .split() 会自动处理空格、换行符、制表符等所有空白字符
    input_data = sys.stdin.read().split()
    
    # 2. 创建一个迭代器
    iterator = iter(input_data)
    
    # 获取第一个数据：容忍值 n
    n = int(next(iterator))
    
    # 获取接下来的 168 个数据（7*24）
    nums = [int(next(iterator)) for _ in range(168)]
        
    # --- 核心算法逻辑 (滑动窗口) ---
    
    length = len(nums) # 固定 168
    
    # 这里的 nums * 2 是为了处理“循环数组”
    # 比如 [1, 2, 3] 变成 [1, 2, 3, 1, 2, 3]
    # 这样原本跨越末尾的区间（如索引 167 到 0）在新数组里就是连续的
    arr = nums * 2
    
    left = 0
    current_sum = 0
    max_len = 0
    
    # 初始化结果
    ans_start = -1
    ans_end = -1
    
    # 右指针遍历扩展后的数组
    for right in range(len(arr)):
        current_sum += arr[right]
        
        # 当窗口和超过容忍值 n 时，左指针收缩
        while current_sum > n:
            current_sum -= arr[left]
            left += 1
        
        # 限制：窗口长度不能超过原本的周期长度 (168)
        # 虽然逻辑上只要 n 合理不太会超, 但在全0或 n很大的情况下需要此限制
        if (right - left + 1) > length:
            current_sum -= arr[left]
            left += 1
            
        current_len = right - left + 1
        
        # 更新最大长度
        # 注意使用 > 而不是 >=, 确保在长度相同时保留“起始下标最小”的那个
        # 因为我们是从左向右遍历的, 先遇到的肯定是下标更小的
        if current_len > max_len:
            max_len = current_len
            # 对下标取模，还原回 0-167 的范围
            ans_start = left % length
            ans_end = right % length
            
    # 输出结果
    if ans_start != -1:
        print(f"{ans_start} {ans_end}")
    else:
        print("-1 -1")

if __name__ == "__main__":
    solve()