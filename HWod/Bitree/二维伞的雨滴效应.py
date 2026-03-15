import sys
sys.setrecursionlimit(10000)

def solve():
    nums = list(map(int, input().split()))
    
    # 1. 验证是否为BST前序遍历（单调栈）
    def is_bst_preorder(nums):
        stack = []
        lower = float('-inf')
        for num in nums:
            if num < lower:  # 比下界小
                return False
            while stack and num > stack[-1]:  # 比栈顶大, 一直弹
                lower = stack.pop()  # 最近一次右转时经过的那个祖先
            stack.append(num)
        return True
    
    if not is_bst_preorder(nums):
        print("0 0 0")
        return
    
    # 2. 构建BST（迭代插入）
    class Node:  # 二叉树的节点定义
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None
    
    def insert(root, val):
        node = Node(val)  # node是要插入的新节点
        if not root:  # 第一次插, 树是空的
            return node
        cur = root
        while True:
            if val < cur.val:  # 小的在左边
                if not cur.left:
                    cur.left = node
                    break
                cur = cur.left  
            else:
                if not cur.right:
                    cur.right = node
                    break
                cur = cur.right
        return root
    
    root = None
    for num in nums:
        root = insert(root, num)
    
    # 3. 收集所有叶子节点（迭代DFS）
    leaves = []
    stack = [root]
    while stack:
        node = stack.pop()
        if not node.left and not node.right:  # 左右都空, 说明是叶子
            leaves.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    # 4. 计算左右伞坠
    # 左伞坠：根有左子树时，叶子最小值（BST中即左侧叶子）
    # 右伞坠：根有右子树时，叶子最大值（BST中即右侧叶子）
    left_p  = min(leaves) if root.left  else 0
    right_p = max(leaves) if root.right else 0
    
    print(f"1 {left_p} {right_p}")

solve()