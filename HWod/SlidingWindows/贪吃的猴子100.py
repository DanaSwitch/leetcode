"""
思路: 从两端取n次 --> 不取中间连续的(len - n)次
      转化为找最小和的滑动窗口问题
"""
def max_bananas():
    n = int(input())
    numbers = list(map(int, input().split()))
    k = int(input())
    
    total = sum(numbers)
    m = n - k  # 窗口长度
    
    # 特殊情况：全部取走
    if m <= 0:
        print(total)
        return
    
    # 滑动窗口找最小子数组和
    window_sum = sum(numbers[:m])  # 初始化
    min_sum = window_sum
    
    for i in range(m, n):
        window_sum = window_sum +  numbers[i] - numbers[i - m]
        min_sum = min(min_sum, window_sum)
    
    print(total - min_sum)

max_bananas()