import sys

def solve():
    input_data = sys.stdin.readline().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    target = int(input_data[1])
    nums = list(map(int, sys.stdin.readline().split()))

    count = 0
    current_sum = 0
    left = 0
    
    # 典型的滑动窗口 (Sliding Window)
    # 只要 [left, right] 的和 >= x，那么以 left 开头
    # 结尾为 right, right+1, ..., n-1 的所有区间都满足条件
    for right in range(n):  # 右指针移动
        current_sum += nums[right]
        
        while current_sum >= target:
            # 关键逻辑：如果当前和满足条件
            # 那么从当前 right 到数组末尾的所有位置作为终点都成立
            count += (n - right)  # 都是正整数, 区间越长, 和越大
            
            # 缩小左边界，尝试寻找下一个满足条件的起始点
            current_sum -= nums[left]
            left += 1
            
    print(count)

if __name__ == "__main__":
    solve()
