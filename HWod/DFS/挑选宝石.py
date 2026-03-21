# 读取输入
n, x, y = map(int, input().split())  # 宝石总数量, 可选宝石数, 属性值
gems = list(map(int, input().split()))

count = 0  # 记录满足条件的方案数

def dfs(start, selected):
    global count
    
    # 已经选够x个了，计算乘积
    if len(selected) == x:
        product = 1  # 初始属性值
        for val in selected:
            product *= val
        if product >= y:
            count += 1
        return

    # 从start位置开始往后挑宝石
    for i in range(start, n):
        selected.append(gems[i])   # 选第i个宝石
        dfs(i + 1, selected)       # 继续往后选
        # 能到这一步说明dfs()已经递归返回了, 所有的可能都尝试了一遍
        selected.pop()             # 撤销选择，尝试下一个

dfs(0, [])
print(count)