def solve(version1, version2):
    v1_parts = list(map(int, version1.split('.')))
    v2_parts = list(map(int, version2.split('.')))

    max_len = max(len(v1_parts), len(v2_parts))
    v1_parts += [0] * (max_len - len(v1_parts))
    v2_parts += [0] * (max_len - len(v2_parts))

    if v1_parts >= v2_parts:
        return 0

    # 找第一个不同段
    first_diff = -1
    for i in range(max_len):
        if v1_parts[i] != v2_parts[i]:
            first_diff = i
            break

    # 题目要求: 检查version2后续是否全为0
    if not all(x == 0 for x in v2_parts[first_diff + 1:]):
        return 0

    return v2_parts[first_diff] - v1_parts[first_diff] - 1

version1, version2 = input().strip().split(',')
print(solve(version1, version2))