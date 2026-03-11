import sys

def dfs(row, limit):
    """深度优先搜索寻找增广路径"""
    for col in range(m):  # 找列
        # col没访问, 且满足条件
        if not visited[col] and matrix[row][col] <= limit:
            visited[col] = True
            # col未使用，或对应行可以修改为其它列
            if match[col] == -1 or dfs(match[col], limit):
                match[col] = row
                return True
    return False

def is_valid(limit):
    """检查是否能找到至少 (n - k + 1) 对匹配"""
    global match, visited
    match = [-1] * m  # match[i] 表示第i列被谁占用了
    match_count = 0
    for row in range(n):
        visited = [False] * m
        if dfs(row, limit):
            match_count += 1
    # 从后往前数第 K 个数，就是从前往后数第 N-K+1 个数
    return match_count >= n - k + 1

# 读取输入
n, m, k = map(int, sys.stdin.readline().split())  # 行, 列
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

min_value, max_value = 1, max(max(row) for row in matrix)  # 搜索下界, 搜索上界

# 二分查找
while min_value <= max_value:
    mid = (min_value + max_value) // 2
    if is_valid(mid):
        max_value = mid - 1
    else:
        min_value = mid + 1

print(min_value)