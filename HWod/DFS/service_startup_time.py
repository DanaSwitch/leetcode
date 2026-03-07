import sys

def get_ready_time(i, use_time, memo, n):
    if i in memo:
        return memo[i]
    
    self_cost = use_time[i][i]
    dependencies = [j for j in range(n) if j != i and use_time[i][j] == 1]
    
    if not dependencies:
        result = self_cost
    else:
        result = self_cost + max(get_ready_time(j, use_time, memo, n) for j in dependencies)
    
    memo[i] = result  # memo[i] 记录的是服务i的完成时间(包括依赖的)
    return result

def main():
    line = sys.stdin.readline()
    n = int(line.strip())
    
    # 逐行读取矩阵
    use_time = []
    for _ in range(n):
        row = list(map(int, sys.stdin.readline().split()))
        use_time.append(row)
    
    # 读取最后一行：目标服务 k
    line = sys.stdin.readline()

    target_k = int(line.strip()) - 1  # 索引从0开始
    
    memo = {}
    print(get_ready_time(target_k, use_time, memo, n))

if __name__ == "__main__":
    main()