import sys

def solve():
    # 读取关系总数
    n = int(sys.stdin.readline().strip())
    
    adj = {}    # 邻接表：记录每个人的朋友集合, 如 {'A': {'B', 'C'}, 'B': {'A'}, ...}
    nodes = set()  # 所有出现过的人名
    
    # 逐行读取朋友关系
    for _ in range(n):
        a, b = sys.stdin.readline().strip().split(',')
        nodes.add(a)
        nodes.add(b)
        # 无向图：A是B的朋友，B也是A的朋友，双向都要加
        adj.setdefault(a, set()).add(b)
        adj.setdefault(b, set()).add(a)
    
    # 确保每个人都在邻接表中（防止某人只出现在nodes但不在adj里）
    for node in nodes:
        adj.setdefault(node, set())
    
    max_circle = []  # 存储找到的所有极大团（朋友圈）
    
    # Bron-Kerbosch 算法：枚举所有极大团
    # 参数说明：
    #   R：当前已确定在团内的节点集合
    #   P：还可以加入团的候选节点集合
    #   X：已经处理过、不能再加入的节点集合
    def bron_kerbosch(R, P, X):
        # 终止条件：P和X都为空，说明R已经是一个极大团（无法再扩展）
        if not P and not X:
            if len(R) >= 3:  # 题目要求至少3人才算朋友圈
                max_circle.append(frozenset(R))
            return
        
        # 选择"枢轴节点" pivot：从 P∪X 中选一个与P中节点共同好友最多的人
        # 目的：跳过 pivot 的所有候选好友，大幅减少递归次数（剪枝优化）
        pivot = max(P | X, key=lambda v: len(adj[v] & P))
        
        # 只遍历 P 中不是 pivot 好友的节点（pivot的好友已被剪枝跳过）
        for v in list(P - adj[pivot]):
            bron_kerbosch(
                R | {v},          # 将 v 加入当前团
                P & adj[v],       # 新候选集 = 原候选集 ∩ v的好友（必须和v也是朋友才能入团）
                X & adj[v]        # 新排除集 = 原排除集 ∩ v的好友
            )
            P = P - {v}   # v 处理完毕，从候选集移除
            X = X | {v}   # 将 v 加入排除集，避免后续重复生成包含 v 的团
    
    # 初始调用：R为空，P为全部节点，X为空
    bron_kerbosch(set(), set(nodes), set())
    
    print(len(max_circle))

solve()