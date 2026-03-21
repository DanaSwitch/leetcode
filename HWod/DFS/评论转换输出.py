"""
输入:
评论1, 回复评论1的数量, 评论2, 回复评论2的数量,...
输出:
首先打印评论嵌套的最大深度。 然后是打印n行, 第 i (1 ≤ i ≤ n) 行对应于嵌套级别为 i 的评论 
(根评论的嵌套级别为1)。 
对于第 i 行，嵌套级别为的评论按照它们出现的顺序打印，用空格分隔开
"""
from collections import deque
import sys

def dfs(pq, res, level):
    if len(res) < level:
        res.append([])
    """
    res 是一个列表的列表
    res = [
    ['hello', 'test', 'one'],   # res[0] → 第1层
    ['ok', 'bye', 'two'],       # res[1] → 第2层
    ['a']                        # res[2] → 第3层
    ]
    """
    comment = pq.popleft()
    sub_count = int(pq.popleft())
    res[level-1].append(comment)  # res[0]表示第一层

    for _ in range(sub_count):
        dfs(pq, res, level + 1)

if __name__ == "__main__":
    nums = sys.stdin.readline().strip().split(',')
    pq = deque(nums)
    res = []
    while pq:
        dfs(pq, res, 1)  # 根评论的层次为1
    print(len(res))
    for row in res:
        print(" ".join(row))