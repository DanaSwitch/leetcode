"""
哈夫曼树的中序遍历
输入:
5
5 15 40 30 10
输出: 40 100 30 60 15 30 5 15 10
"""
import heapq

class Node:
    def __init__(self, weight, left=None, right=None):
        self.weight = weight
        self.left = left
        self.right = right
        # 叶子节点高度为1, 内部节点取左右子树最大高度+1
        lh = left.height if left else 0
        rh = right.height if right else 0
        self.height = 1 + max(lh, rh)

    def __lt__(self, other):  # less than自定义小于
        # 堆的排序: 先按权值, 权值相同按高度
        if self.weight != other.weight:
            return self.weight < other.weight
        return self.height < other.height

# 递归: 左根右
def inorder(node, result):
    if node is None:
        return
    inorder(node.left, result)
    result.append(node.weight)
    inorder(node.right, result)

# 读取输入
n = int(input())  # 叶子节点个数
weights = list(map(int, input().split()))  # 叶子节点权重

# 初始化最小堆
heap = []
for w in weights:
    heapq.heappush(heap, Node(w))
    
# 构建哈夫曼树
while len(heap) > 1:
    a = heapq.heappop(heap)  # 较小权值（或相同权值中较小高度）
    b = heapq.heappop(heap)  # 较大权值（或相同权值中较大高度）
    # a作左子树(≤)，b作右子树，满足左≤右且等值时左高度≤右高度
    parent = Node(a.weight + b.weight, left=a, right=b)
    heapq.heappush(heap, parent)

# 中序遍历
result = []
inorder(heap[0], result)
print(' '.join(map(str, result)))