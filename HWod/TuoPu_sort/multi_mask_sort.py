"""
思想: 通过每一轮“清理”当前入度为 0 的任务，并实时更新其后续任务的依赖状态,
     在满足字典序的前提下，由浅入深地完成所有任务的拓扑排序。
"""
def getResult():
    # 从标准输入读取依赖字符串，拆分为 [['A', 'B'], ['C', 'D'], ['E', 'F']] 的列表形式
    relations = list(map(lambda s: s.split("->"), input().split())) 

    inDegree = {}   # 记录每个任务当前需要依赖的任务总数（入度）
    next_tasks = {} # 记录每个任务完成后，可以触发的后续任务列表（邻接表）

    for a, b in relations:  # 两两解包
        # 确保所有涉及的任务都在字典中, 避免后续访问 Key Error
        if a not in inDegree: inDegree[a] = 0
        if b not in inDegree: inDegree[b] = 0
        
        inDegree[a] += 1  # a 依赖于 b，所以 a 的入度 +1
        
        # 建立 b 到 a 的映射，表示 b 完成后才能轮到 a
        if b not in next_tasks: next_tasks[b] = []
        # 一旦b完成, a就可以开始
        next_tasks[b].append(a)
        
        # 确保所有节点在邻接表中都有定义
        if a not in next_tasks: next_tasks[a] = []

    # 2. 收集初始入度为 0 的任务（即没有任何依赖的“起点”任务）
    queue = [task for task in inDegree if inDegree[task] == 0]
    
    ans = []
    # 拓扑排序主循环：只要还有可执行的任务
    while queue:
        # 根据题目要求，同一层级的任务按字母顺序排序执行
        queue.sort()  # 字母排序
        
        newQueue = [] # 用于存放下一轮解锁的任务
        for father in queue:
            ans.append(father) # 将当前任务加入执行序列
            
            # 遍历当前任务 fa 指向的所有子任务 ch
            for ch in next_tasks.get(father, []):
                # fa 执行完毕，ch 的依赖数 -1
                inDegree[ch] -= 1
                # 如果 ch 的依赖全部解除，则将其加入下一轮待执行队列
                if inDegree[ch] == 0:
                    newQueue.append(ch)
                
        queue = newQueue  # 更新队列，进入下一层处理

    return " ".join(ans)

print(getResult())