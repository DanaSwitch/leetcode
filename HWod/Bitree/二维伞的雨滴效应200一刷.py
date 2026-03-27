import sys
sys.setrecursionlimit(10000)

def solve():
    nums = list(map(int, input().split()))  # 读入数组
    
    # 节点定义
    class Node:
        def __init__(self, data):
            self.data = data            # 节点的值
            self.left = self.right = None  # 左右孩子初始为空
    
    # 插入节点：小的放左边，大的放右边
    def insert(root, data):
        if not root: return Node(data)  # 空位，直接放这里
        if data < root.data: root.left = insert(root.left, data)   # 小 → 去左边
        else: root.right = insert(root.right, data)                # 大 → 去右边
        return root  # 把自己返回给父节点挂上
    
    # 建树
    root = None
    for n in nums: root = insert(root, n)
    
    # 前序遍历：根 → 左 → 右
    def preorder(node, res):
        if not node: return
        res.append(node.data)       # 先记录根
        preorder(node.left, res)    # 再遍历左
        preorder(node.right, res)   # 最后遍历右
    
    res = []
    preorder(root, res)
    
    # 验证：把树的前序遍历和输入对比，一样说明是BST
    if res != nums:
        print("0 0 0")
        return
    
    # 收集所有叶子节点（左右都空的节点）
    def leaves(node, res):
        if not node: return
        if not node.left and not node.right:  # 是叶子 → 收集
            res.append(node.data)
            return
        leaves(node.left, res)   # 去左边找叶子
        leaves(node.right, res)  # 去右边找叶子
    
    ls = []
    leaves(root, ls)
    
    # 左伞坠 = 最小叶子（BST性质保证），根没有左子树则为0
    # 右伞坠 = 最大叶子（BST性质保证），根没有右子树则为0
    left_p  = min(ls) if root.left  else 0
    right_p = max(ls) if root.right else 0
    print(f"1 {left_p} {right_p}")

solve()