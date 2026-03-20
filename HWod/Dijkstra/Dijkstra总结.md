### visited的区别

**BFS 的 visited** — 只需记录"来过没有"，因为 BFS 第一次到达某节点时路径就一定是最短的，之后再来只会更差，直接拦住。

```python
visited = [[False] * n for _ in range(m)]
visited[0][0] = True
# 到达(nx, ny)时：
if not visited[nx][ny]:
    visited[nx][ny] = True
```

**Dijkstra 的 visited** — 要记录"到达这里的最短时间"，因为第一次到达某节点时不一定最优（后续可能有耗时更少的路径绕过来），需要比较才能决定要不要更新。

```python
visited = [[float('inf')] * n for _ in range(m)]
visited[0][0] = 0
# 到达(nx, ny)时：
if visited[nx][ny] > next_time:   # 发现更短的就更新
    visited[nx][ny] = next_time
```

本质原因是：

- BFS 每步代价**相同**，先到一定最优，`bool` 够用
- Dijkstra 每步代价**不同**，先到不一定最优，需要记录具体数值来比较