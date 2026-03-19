def backtrack(segments, used, side_length_set):
    """
    递归回溯枚举三条边，并使用剪枝算法
    """
    res = 0
    n = len(segments)
    for i in range(n - 2):
        if used[i]:
            continue  # 已使用
        for j in range(i + 1, n - 1):
            if used[j]:
                continue  # 已使用
            # 第三条边长度平方
            c = segments[i] + segments[j]
            # 不存在指定边，剪枝
            if c not in side_length_set:
                continue
            for k in range(j + 1, n):
                if used[k]:
                    continue
                # 剪枝：segments 是递增的，后续不可能等于 c 的边
                if segments[k] > c:
                    break
                if segments[k] != c:
                    continue
                # 递归回溯
                used[i] = used[j] = used[k] = True
                res = max(res, backtrack(segments, used, side_length_set) + 1)
                used[i] = used[j] = used[k] = False
    return res


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        n = arr[0]
        raw_lengths = arr[1:]
        # 存储输入边的平方，因为判断直接公式 a^2 + b^2 = c^2
        side = [x * x for x in raw_lengths]
        # 记录出现的边长平方，用于后续剪枝
        side_length_set = set(side)
        # 排序
        side.sort()
        # 标记是否被使用
        used = [False] * n
        res = backtrack(side, used, side_length_set)
        print(res)