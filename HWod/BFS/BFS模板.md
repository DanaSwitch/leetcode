# BFS模板

## 常见应用

最短路径(无权图)，矩阵扩散问题，状态搜索



## 模板

### 1.基础BFS模板(普通图遍历)

> 队列初始化
> while 队列:
>     取出节点
>     遍历邻居
>         如果没访问
>             标记
>             入队

```python
from collections import deque

def bfs(start):
    queue = deque([start])
    visited = set([start])

    while queue:
        node = queue.popleft()

        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                queue.append(nei)
```



### 2.最短路径BFS

无权图最短路径，最少步数问题

> 队列存 (节点, 步数)

华为od C卷：自动泊车

```python
from collections import deque

def bfs(start):
    queue = deque([(start, 0)])
    visited = set([start])

    while queue:
        node, step = queue.popleft()

        if node == target:  # 到底目的地
            return step

        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                queue.append((nei, step + 1))
```



### 3.矩阵BFS模板

> 岛屿问题，扩散问题，迷宫问题

```python
from collections import deque

def bfs(grid, i, j):
    m, n = len(grid), len(grid[0])  # 行, 列
    queue = deque([(i, j)])
    visited = set([(i, j)])  # 集合去重

  	dirs = [(-1,0), (1,0), (0,-1), (0,1)]  # 上下左右

    while queue:
        x, y = queue.popleft()  # 取出当前坐标

        for dx, dy in dirs:  # 扩散
            nx, ny = x + dx, y + dy

            if 0 <= nx < m and 0 <= ny < n:  # 在矩阵内且没被访问
                if (nx, ny) not in visited:
                    visited.add((nx, ny))  # 标记为已访问
                    queue.append((nx, ny))  # 加入队列
```





### 4.多源BFS

> 应用：腐烂橘子，01矩阵，最近距离，火焰扩散

华为od C卷：矩阵扩散

思想：多个起点同时入队，一起扩散

```python
from collections import deque

def multi_bfs(grid):
    m, n = len(grid), len(grid[0])  # 行, 列
    queue = deque()

    # 所有起点入队
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:   # 起点条件
                queue.append((i, j))

    dirs = [(-1,0), (1,0), (0,-1), (0,1)]  # 上下左右

    step = 0  # 感染距离

    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n:
                    if grid[nx][ny] == 0:
                        grid[nx][ny] = 1
                        queue.append((nx, ny))

        step += 1
```



### 5.连通分量

> 华为od C卷：可以组成网络的服务器

```python
from collections import deque

n,m=map(int,input().split())
g=[list(input()) for _ in range(n)]
vis=[[0]*m for _ in range(n)]
d=[(1,0),(-1,0),(0,1),(0,-1)]

def bfs(i,j):
    q=deque([(i,j)])
    vis[i][j]=1
    while q:
        x,y=q.popleft()
        for dx,dy in d:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<m and not vis[nx][ny] and g[nx][ny]=='1':
                vis[nx][ny]=1
                q.append((nx,ny))

ans=0
for i in range(n):
    for j in range(m):
        if g[i][j]=='1' and not vis[i][j]:
            bfs(i,j)
            ans+=1

print(ans)
```



> 1 1 0 0 0
> 1 1 0 1 1
> 0 0 0 1 1
> 0 1 0 0 0
> 0 1 1 0 0
>
> A A . . .
> A A . B B
> . . . B B
> . C . . .
> . C C . .
>
> `A` 是一块连通区域
>
> `B` 是一块连通区域
>
> `C` 是一块连通区域







### 6.BFS 层序遍历模板（树）

> 应用：二叉树层序遍历，按层处理问题

```python
from collections import deque

def bfs(root):
    queue = deque([root])

    while queue:
        size = len(queue)

        for _ in range(size):
            node = queue.popleft()

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)
```



