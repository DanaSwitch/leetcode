# DFS模板

### 模板

```python
def backtrack(候选集, 路径, 深度):
    # 1. 终止条件：如果不满足题目要求，或者选够了，就停止
    if 达到终止条件:
        处理结果
        return

    # 2. 遍历候选集：尝试所有可能的选择
    for i in range(start, len(候选集)):
        # 做选择
        路径.append(候选集[i])
        
        # 递归：进入下一层去选下一个
        backtrack(候选集, 路径, i + 1)
        
        # 撤销选择（回溯的关键）：把刚刚尝试的路删掉，换下一条路
        路径.pop()
```



### 例题

> 题目描述
>
> 游乐园有一款互动游戏，游戏开始时会提供n个宝石，每个宝石都一个属性值a1,a2,...an.玩家在游戏前可以挑选x颗宝石，将这些宝石的属性值相乘组成玩家的属性值。游戏玩家需要y点属性值，请帮助游戏玩家计算有多少种计算方式。
>
> 输入描述
>
> 第一行：三个整数n,x,y
>
> - 第一个整数n(0 < n <20)表示宝石总数量。
> - 第二个整数x(0<x <=n)，表示可以选择宝石个数
> - 第三个整数y，表示通过游戏需要的属性值
>
> 第二行：n个整数，a1,a2,...an(-100 < ai < 100)，表示每个宝石的属性值。
>
> 输出描述
>
> 输出一个整数，表示玩家可以通过游戏的挑选方式的数量。
>
> 用例1
>
> 输入
>
> ```none
> 4 2 8
> 2 -3 4 5
> ```
>
> 输出
>
> ```none
> 3
> ```

```python
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
    
    # 2层以上, 从start位置开始往后挑宝石
    for i in range(start, n):
        selected.append(gems[i])   # 选第i个宝石
        dfs(i + 1, selected)       # 继续往后选
        # 能到这一步说明dfs()已经递归返回了, 所有的可能都尝试了一遍
        selected.pop()             # 撤销选择，尝试下一个

dfs(0, [])
print(count)
```

