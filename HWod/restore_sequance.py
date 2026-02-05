import sys

def get_digit_counts(n):
    """手动统计单个数字中各数位的频次"""
    counts = [0] * 10  # 0-9
    for char in str(n):
        counts[int(char)] += 1
    return counts

def solve():
    # 读取输入
    input_data = sys.stdin.read().split()  # spilt是按空格, 换行将输入分开
    if not input_data:
        return
    
    shuffled_str = input_data[0]
    k = int(input_data[1])
    
    # 1. 目标频次统计
    target_counts = [0] * 10
    for char in shuffled_str:
        target_counts[int(char)] += 1
    
    # 2. 初始化窗口（起始序列为 1 到 k）
    current_counts = [0] * 10
    for i in range(1, k + 1):
        for char in str(i):
            current_counts[int(char)] += 1
            
    # 3. 滑动窗口
    # 根据题目约束，正整数不超过 1000，我们枚举起始数字 s
    for s in range(1, 1001):
        # 检查当前窗口是否匹配
        if current_counts == target_counts:
            print(s)
            return
        
        # 窗口向右滑动：移出 s, 移入 s + k
        # 减去即将离开窗口的 s 的贡献
        for char in str(s):
            current_counts[int(char)] -= 1
        
        # 加上新进入窗口的 s + k 的贡献
        for char in str(s + k):
            current_counts[int(char)] += 1

if __name__ == "__main__":
    solve()