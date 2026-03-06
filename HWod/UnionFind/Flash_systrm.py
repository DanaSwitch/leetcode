import sys

# 查找代表节点（路径压缩）
def find(a, parent):
    if parent[a] != a:  # 至到找到根节点退出
        parent[a] = find(parent[a], parent)
    return parent[a]

# 合并两个集合
def union(a, b, parent):
    ra = find(a, parent)
    rb = find(b, parent)
    new_root = min(ra, rb)  # 索引最小的作为新的根节点
    parent[ra] = new_root
    parent[rb] = new_root

def main():
    # 不知道读多少行, 索性一次性全部读取
    lines = sys.stdin.read().strip().splitlines()  # splitlines() 只按照换行进行分割
    if not lines:
        return

    m = int(lines[0])
    n = int(lines[1])

    martix = [-1] * (m * n)  # 初始化矩阵
    # 四个方向, 上下左右
    dirs = [(-1,0), (1,0), (0,-1), (0,1)]

    block_count = 0  # 坏块数量
    result = []  # result[i] 表示i时刻坏块的数量

    for line in lines[2:]:
        if not line.strip():  # 如果这一行是空的, 跳过
            continue

        row, col = map(int, line.split(','))
        id = row * n + col  # 二维转化为一维
        # 已经是异常，不会影响
        if martix[id] != -1:
            result.append(block_count)
            continue
        """
        刚开始时, 自己就是自己的根, 合并时才会更新根节点
        """
        martix[id] = id  # martix[id] 表示 id 的父节点
        block_count += 1

        for dr, dc in dirs:  # 上下左右遍历
            nr, nc = row + dr, col + dc
            # 越界就跳过
            if nr < 0 or nr >= m or nc < 0 or nc >= n:
                continue

            nid = nr * n + nc
            # 不是异常的
            if martix[nid] == -1:
                continue
            # 不属于同一个异常块, 但是相邻就合并, 异常块数量-1
            if find(id, martix) != find(nid, martix):
                union(id, nid, martix)
                block_count -= 1

        result.append(block_count)

    print("[" + ",".join(map(str, result)) + "]")  # join只能用字符串

if __name__ == "__main__":
    main()