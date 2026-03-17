import heapq

def solve():

    line1 = input().split()
    if not line1: return
    n, m = map(int, line1)
    lights = [list(map(int, input().split())) for _ in range(n)]
    T = int(input())
    rs, cs = map(int, input().split())
    re, ce = map(int, input().split())
    
    # 右, 下, 左, 上 (顺时针)
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # pq: (cost, r, c, direction)
    pq = []
    # dist[r][c][dir]
    dist = [[[float('inf')] * 4 for _ in range(m)] for _ in range(n)]

    # 起点向四个方向出发，第一步不计等灯时间
    for d in range(4):
        nr, nc = rs + dirs[d][0], cs + dirs[d][1]
        if 0 <= nr < n and 0 <= nc < m:
            dist[nr][nc][d] = T
            heapq.heappush(pq, (T, nr, nc, d))

    ans = float('inf')
    if rs == re and cs == ce:
        print(0)
        return

    while pq:
        d_cost, r, c, d = heapq.heappop(pq)

        if d_cost > dist[r][c][d]:
            continue
        
        if r == re and c == ce:
            ans = min(ans, d_cost)
            continue

        for nd in range(4):
            nr, nc = r + dirs[nd][0], c + dirs[nd][1]
            if 0 <= nr < n and 0 <= nc < m:
                turn = (nd - d + 4) % 4
                
                # 0:直行, 1:右转, 2:掉头, 3:左转
                # 只有右转 (1) 不需要等待
                wait = 0 if turn == 1 else lights[r][c]
                new_cost = d_cost + wait + T
                
                if new_cost < dist[nr][nc][nd]:
                    dist[nr][nc][nd] = new_cost
                    heapq.heappush(pq, (new_cost, nr, nc, nd))

    print(ans)

solve()