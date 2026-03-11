"""
思路: 两次循环调用, 第一次遍历所有员工, 第二次遍历每个员工影响的人
"""
def solve():
    n = int(input())
    graph = []
    for _ in range(n):
        line = input().strip()
        if line == '*':
            graph.append([])
        else:
            graph.append(list(map(int, line.split())))
    
    def dfs(node, visited):
        for neighbor in graph[node]:  # 遍历node中有的员工
            if neighbor not in visited:  # 没访问过
                visited.add(neighbor)
                dfs(neighbor, visited)  # 递归深入影响链
    
    scores = []
    for i in range(n):
        visited = {i}          # 从自身出发，自身不计分
        dfs(i, visited)
        scores.append(len(visited) - 1)
    
    print(' '.join(map(str, scores)))

solve()