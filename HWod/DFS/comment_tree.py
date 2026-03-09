from collections import deque
import sys

def dfs(pq, res, level):
    if len(res) < level:
        res.append([])
    
    comment = pq.popleft()
    sub_count = int(pq.popleft())  # 对于要进行数字比较的, 改为int
    res[level-1].append(comment)

    for _ in range(sub_count):
        dfs(pq, res, level + 1)

if __name__ == "__main__":
    nums = sys.stdin.readline().strip().split(',')
    pq = deque(nums)
    res = []
    while pq:
        dfs(pq, res, 1)
    print(len(res))
    for row in res:
        print(" ".join(row))