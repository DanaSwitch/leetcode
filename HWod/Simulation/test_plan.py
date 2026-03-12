import sys

n, m = map(int, sys.stdin.readline().split())  # 特性数量, 测试用例数量

priority = [0]  # 转化为1开头的下标
for _ in range(n):
    priority.append(int(sys.stdin.readline().strip()))

test_case = []  # 存放测试用例(优先级, 下标)

for i in range(m):
    choose_case = list(map(int, sys.stdin.readline().split()))
    total_priority = 0
    for idx in choose_case:
        total_priority += priority[idx]  # 测试用例的优先级

    test_case.append((total_priority, i + 1))  # (优先级, 下标)

# 排序：优先级降序，编号升序
test_case.sort(key=lambda x: (-x[0], x[1]))

# 输出2
for _, idx in test_case:
    print(idx)