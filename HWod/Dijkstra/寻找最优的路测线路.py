import heapq

def solve():
    R = int(input())
    C = int(input())
    grid = []
    for _ in range(R):
        row = list(map(int, input().split()))
        grid.append(row)
    
    # 最大堆（用负值模拟）
    # (负的路径最小值, 行, 列)
    heap = [(-grid[0][0], 0, 0)]  # (-信号值, 坐标)
    visited = [[False] * C for _ in range(R)]
    
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    
    while heap:
        neg_score, r, c = heapq.heappop(heap)
        score = -neg_score
        
        if visited[r][c]:
            continue
        visited[r][c] = True
        
        # 到达终点
        if r == R-1 and c == C-1:
            print(score)
            return
        # 每一步只扩展当前最优的节点
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
                new_score = min(score, grid[nr][nc])
                # 保存所有候选集合, 先尝试最大的
                heapq.heappush(heap, (-new_score, nr, nc))

solve()