"""
第一道题是给几条路径，然后给个出发点和终点，求从出发点到终点的路径，
最后返回一个字典序最小的路径，路径出发点这些都是字符串
"""
def solve():
    # 1. 处理输入
    # 假设输入格式：第一行是路径数量n，接下来n行是 "A B" 表示A到B有路
    # 最后一行是 "起点 终点"

    n = int(input().strip())
    adj = {}
    for _ in range(n):
        u, v = input().split()
        if u not in adj: adj[u] = []
        if v not in adj: adj[v] = [] # 保证终点也在字典里
        adj[u].append(v)
    
    start_node, end_node = input().split()

    # 2. 核心步骤：对邻居节点进行字典序排序
    # 这样我们在DFS时，会优先走字母表靠前的路径
    for key in adj:
        adj[key].sort()

    res = [] # 存储最终找到的第一条路径（即字典序最小路径）

    # 3. DFS 搜索
    # path: 当前走过的路径列表
    # visited: 当前路径已访问的点，防止走回头路
    def dfs(curr, target, path, visited):
        # 如果已经找到了一条路径，直接返回（因为排序过，第一条就是最优解）
        if res: 
            return
        
        # 到达终点
        if curr == target:
            res.extend(list(path))
            return
        
        # 遍历邻居
        for neighbor in adj.get(curr, []):
            if neighbor not in visited:
                visited.add(neighbor)
                path.append(neighbor)
                
                dfs(neighbor, target, path, visited)
                
                # 回溯
                path.pop()
                visited.remove(neighbor)

    # 启动搜索
    dfs(start_node, end_node, [start_node], {start_node})

    # 4. 输出结果
    if res:
        print(" ".join(res))
    else:
        # 如果没找到路径（视题目要求输出，通常是空或特定字符串）
        print("")

if __name__ == "__main__":
    solve()