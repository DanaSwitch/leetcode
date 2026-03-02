import sys

# 设置递归深度限制，防止处理大数据时报错（虽然这题 n 只有 500）
sys.setrecursionlimit(2000)

def solve():
    # 读取输入
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    literator = iter(input_data)
    n = int(next(literator))


    # 记账本：memo[x] 存储数字 x 作为开头时，能形成的合法数列个数
    memo = {}

    def count_sequences(current_val):
        # 如果已经算过这个数了，直接返回结果
        if current_val in memo:
            return memo[current_val]
        
        # 初始方案数：只有它自己一个数的数列（比如 [7]）
        total = 1
        
        # 寻找接班人：从 1 到 current_val // 2
        max_next = current_val // 2
        for next_val in range(1, max_next + 1):
            total += count_sequences(next_val)
        
        # 记入账本并返回
        memo[current_val] = total
        return total

    # 从 n 开始计算
    print(count_sequences(n))

if __name__ == "__main__":
    solve()