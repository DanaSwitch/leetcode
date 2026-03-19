def solve():
    arr = list(map(int, input().split()))
    n = len(arr)

    def get_node(idx):
        """获取1-based下标idx的节点值，越界或为-1均视为空"""
        if idx < 1 or idx > n:
            return -1
        return arr[idx - 1]

    def is_leaf(idx):
        """判断节点是否为叶子节点"""
        return get_node(2 * idx) == -1 and get_node(2 * idx + 1) == -1

    min_leaf_val = float('inf')
    min_leaf_path = []

    def dfs(idx, path):
        nonlocal min_leaf_val, min_leaf_path
        val = get_node(idx)
        if val == -1:
            return
        path.append(val)
        if is_leaf(idx):
            if val < min_leaf_val:
                min_leaf_val = val
                min_leaf_path = path[:]
        else:
            dfs(2 * idx, path)
            dfs(2 * idx + 1, path)
        path.pop()

    dfs(1, [])
    print(' '.join(map(str, min_leaf_path)))

solve()