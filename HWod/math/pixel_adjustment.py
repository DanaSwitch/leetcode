import sys

def solve():
    input_line = sys.stdin.readline().strip()
    if not input_line:
        return
    img = list(map(int, input_line.split()))
    
    n = len(img)
    min_diff = float('inf')
    k_ans = 0
    
    # 遍历可能的偏移量 k
    for k in range(-127, 129):
        current_sum = 0
        for val in img:
            # 像素截断处理, 不超过0~255
            new_val = max(0, min(val + k, 255))
            current_sum += new_val
        
        # 计算均值偏差
        mean = current_sum / n  # 旧的平均值
        diff = abs(mean - 128)
        
        # 寻找最小偏差，并处理相同偏差的情况
        if diff < min_diff:
            min_diff = diff
            k_ans = k  # 更新答案
        elif diff == min_diff:
            # 如果偏差相同，取较小的 k
            k_ans = min(k_ans, k)
            
    print(k_ans)

if __name__ == "__main__":
    solve()