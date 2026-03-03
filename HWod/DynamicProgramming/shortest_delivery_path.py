import sys

def main():
    # 1. 读取 n 和 m
    line = sys.stdin.readline().split()
    if not line:
        return
    n, m = map(int, line)

    # 初始化图，索引 0 为投递站，1 到 n 为客户点
    num_nodes = n + 1
    inf = float('inf')
    graph = [[inf] * num_nodes for _ in range(num_nodes)]
    
    for i in range(num_nodes):
        graph[i][i] = 0  # graph[i][j] 表示i到j的距离

    # 离散化 ID 映射，将原始客户 ID 映射为 1 到 n
    mp = {}
    
    # 2. 读取投递站到客户的距离 (n 行)
    for i in range(n):
        row = sys.stdin.readline().split()
        if not row: break
        cid = int(row[0])  # 客户id
        dist = int(row[1])  # 距离
        mp[cid] = i + 1  # 0留给投递站
        # 填充投递站(0)与客户(1~n)的双向距离
        graph[0][mp[cid]] = min(graph[0][mp[cid]], dist)  # 防止输入了多次距离, 所以用min
        graph[mp[cid]][0] = min(graph[mp[cid]][0], dist)

    # 3. 读取客户之间的距离 (m 行), 更新地图graph
    for _ in range(m):
        row = sys.stdin.readline().split()
        if not row: break
        u_id, v_id, dist = map(int, row)
        if u_id in mp and v_id in mp:
            u, v = mp[u_id], mp[v_id]
            graph[u][v] = min(graph[u][v], dist)
            graph[v][u] = min(graph[v][u], dist)

    # 4. Floyd 算法计算全源最短路径
    # 确保客户之间即使没有直连，也能通过其他点中转
    for k in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

    # 5. 状态压缩 DP
    # dp[mask][cur] 表示访问客户状态为 mask，当前位于点 cur
    num_states = 1 << n
    dp = [[inf] * num_nodes for _ in range(num_states)]
    
    # 初始状态：在投递站(0)，尚未访问任何客户(mask=0)
    dp[0][0] = 0

    for mask in range(num_states):  # 从送货少到送货多
        for cur in range(num_nodes):
            if dp[mask][cur] == inf:
                continue
            
            # 尝试前往下一个点 next_node (可以是回站 0，也可以是去客户 1~n)
            for next_node in range(num_nodes):
                d = graph[cur][next_node]
                if d == inf:
                    continue
                
                if next_node == 0:
                    # 回到投递站，已访问客户集合 mask 不变
                    if dp[mask][cur] + d < dp[mask][0]:   # 不断更新记录当前点回站点的距离
                        dp[mask][0] = dp[mask][cur] + d
                else:
                    # 前往客户 next_node，更新 mask
                    # 客户 1 对应 mask 第 0 位，以此类推
                    new_mask = mask | (1 << (next_node - 1))  # 按位或, 更新新客户点
                    if dp[mask][cur] + d < dp[new_mask][next_node]:  # 中间两点距离更小, 则更新
                        dp[new_mask][next_node] = dp[mask][cur] + d

    # 6. 最终结果：所有客户已送达 (mask = (1 << n) - 1) 且回到投递站 (cur = 0)
    final_mask = (1 << n) - 1
    res = dp[final_mask][0]

    if res == inf:
        print("-1")
    else:
        print(int(res))

if __name__ == "__main__":
    main()