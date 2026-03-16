from collections import deque

post, mid = input().split()  # 后序, 中序

def split_tree(post, mid, queue, ans):
    """
    从后序、中序序列中找出根节点，
    并将左、右子树的（后序+中序）序列放入队列等待下一轮处理
    """

    root = post[-1]  # 找出根节点
    ans.append(root)  # 根节点直接加入结果（层序从上到下，根最先）

    # 在中序遍历中找到根节点的位置
    # 根节点左边 = 左子树，根节点右边 = 右子树
    root_idx = mid.find(root)

    left_len = root_idx  # 左子树节点数 = 根节点在中序中的下标

    # 处理左子树（如果左子树存在）
    if left_len > 0:
        # 后: 左右根
        left_post = post[:left_len]   # 后序前 left_len 个属于左子树
        left_mid  = mid[:root_idx]    # 中序根节点左边属于左子树
        queue.append([left_post, left_mid])  # 加入队列，等待后续处理

    # 处理右子树（如果右子树存在）
    right_len = len(post) - 1 - left_len   # 总长度 - 根节点(1) - 左子树长度
    if right_len > 0:
        # 后: 左右根
        right_post = post[left_len:-1]   # 后序中间部分属于右子树（去掉最后的根）
        right_mid  = mid[root_idx + 1:]  # 中序根节点右边属于右子树
        queue.append([right_post, right_mid])  # 加入队列，等待后续处理


def bfs(post, mid):
    """
    层序遍历主流程：
    每次从队列取出一棵子树，找出它的根节点加入结果，
    再把它的左、右子树加入队列 —— 如此循环直到队列为空
    """
    queue = deque()   # BFS 执行队列，存放待处理的 [post, mid] 对
    ans   = []   # 存放层序遍历的结果

    # 从整棵树开始[]
    split_tree(post, mid, queue, ans)

    # 队列不为空就继续处理
    while queue:
        cur_post, cur_mid = queue.popleft()   # 取出队列最前面的子树
        split_tree(cur_post, cur_mid, queue, ans)

    return "".join(ans)


# 输出结果
print(bfs(post, mid))