import sys

# 1. 提高递归深度限制，防止处理大矩阵时报错
sys.setrecursionlimit(10**6)

def solve():
    # 读取所有输入并按空格/换行切分
    data = sys.stdin.readline().split()
    if not data: return
    
    n, m = int(data[0]), int(data[1])
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    # 2. 定义连锁反应函数：消除相连的 1
    def dfs(r, c):
        # 标记当前位置为 0，防止死循环
        grid[r][c] = 0
        
        for dr in [-1, 0, 1]:  # 每行
            for dc in [-1, 0, 1]:  # 每列
                new_r, new_c = r + dr, c + dc
                # 检查：在边界内 且 是 1
                if 0 <= new_r < n and 0 <= new_c < m and grid[new_r][new_c] == 1:
                    dfs(new_r, new_c)

    # 3. 扫描整个矩阵，统计点击次数
    counts = 0
    for r in range(n):
        for c in range(m):
            if grid[r][c] == 1:
                counts += 1
                dfs(r, c)

    print(counts)


if __name__ == "__main__":
    solve()