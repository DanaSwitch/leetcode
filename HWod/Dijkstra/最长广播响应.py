import sys
import heapq

INF = 10**18

# 迪杰斯特拉求最短路径
def dijkstra(start, graph):
    n = len(graph)
    dist = [INF] * n
    dist[start] = 0

    # 最小堆（距离小的优先）
    pq = [(0, start)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue

        # 更新与 u 相连的点
        for v in graph[u]:
            if dist[u] + 1 < dist[v]:
                dist[v] = dist[u] + 1
                heapq.heappush(pq, (dist[v], v))

    # 单向最长时延
    res = 0
    for d in dist:
        if d == INF:
            return -1
        res = max(res, d)
    return res


def main():
    data = list(map(int, sys.stdin.read().split()))
    idx = 0

    n, m = data[idx], data[idx + 1]
    idx += 2

    g = [[] for _ in range(n)]
    for _ in range(m):
        x, y = data[idx], data[idx + 1]
        idx += 2
        g[x - 1].append(y - 1)
        g[y - 1].append(x - 1)

    pos = data[idx]
    res = dijkstra(pos - 1, g)

    # 往返 * 2
    print(res * 2)


if __name__ == "__main__":
    main()