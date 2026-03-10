"""
思路: 在回溯中用共享容器min_dist记录最小路径和, 
"""
if __name__ == "__main__":
    n = int(input())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().strip().split())))
    visited = [False] * n
    min_dist = [float('inf')]  # 最短路径和
    visited[0] = True  # 从起点0开始访问
    count = 1  # 访问基站个数

    def dfs(cur_node, count, cur_sum):
        if count == n:  # 递归出口: 加上回基站1的距离
            # 已经访问完所有的节点了, 只剩下0点, 所以回去直接加就好了
            total_sum = cur_sum + matrix[cur_node][0]
            min_dist[0] = min(min_dist[0], total_sum)
            return
        # 剪枝
        if cur_sum > min_dist[0]:  # 当前路径和超过已经找到的路径和
            return
        
        # 从当前节点遍历所有节点
        for nextnode in range(0, n):
            if not visited[nextnode]:  # 该结点没有访问过    
                visited[nextnode] = True
                dfs(nextnode, count+1, cur_sum + matrix[cur_node][nextnode])
                visited[nextnode] = False

    dfs(0, 1, 0)    
    print(min_dist[0])