import sys

def solve():
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    weights = list(map(int, input_data[1:n+1]))
    
    # 用循环手动算异或，替代 reduce(xor, weights)
    total_xor = 0
    for w in weights:
        total_xor ^= w  # ^= 就是异或运算符
    
    if total_xor != 0:  # 无法满足A的要求平分异或
        print(-1)
        return
    
    total_sum = sum(weights)
    min_weight = min(weights)
    
    print(total_sum - min_weight)

solve()