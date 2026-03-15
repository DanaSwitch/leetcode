def solve():
    n, m = map(int, input().split())  # n行 m列
    lights = [list(map(int, input().split())) for _ in range(n)]
    T = int(input())  # 移动一格的时间
    rs, cs = map(int, input().split())  # 起点(r, c)
    re, ce = map(int, input().split())  # 终点(r, c)

    # 四个方向：右、下、左、上（顺时针）
    dirs = [(0,1), (1,0), (0,-1), (-1,0)]  # 必须是顺时针

    INF = float('inf')
    best = [[[INF] * 4 for _ in range(m)] for _ in range(n)]
    ans = [INF]

    def dfs(r, c, d, cost):
        if r == re and c == ce:
            ans[0] = min(ans[0], cost)
            return

        for nd in range(4):
            nr, nc = r + dirs[nd][0], c + dirs[nd][1]  # ← 改这里
            if not (0 <= nr < n and 0 <= nc < m):
                continue

            turn = (nd - d + 4) % 4
            wait = 0 if turn == 1 else lights[r][c]
            new_cost = cost + wait + T

            if new_cost >= best[nr][nc][nd]:
                continue

            best[nr][nc][nd] = new_cost
            dfs(nr, nc, nd, new_cost)

    # 起点不等灯，直接走出去
    for d in range(4):
        nr, nc = rs + dirs[d][0], cs + dirs[d][1]  # ← 改这里
        if 0 <= nr < n and 0 <= nc < m:
            best[nr][nc][d] = T
            dfs(nr, nc, d, T)

    print(ans[0])

solve()