import sys

first = input().split(',')
M, N = int(first[0]), int(first[1])

if not (3 <= M <= 10) or not (3 <= N <= 100):
    print(-1)
    sys.exit()

scores = []
for _ in range(M):
    row = list(map(int, input().split(',')))  # sorce[j][i]表示评委j给选手(i+1)的分
    if len(row) != N or any(not (1 <= s <= 10) for s in row):
        print(-1)
        sys.exit()
    scores.append(row)

# 总分
total = [0] * N
for i in range(N):
    for j in range(M):
        total[i] += scores[j][i]

# 各分值计数：counts[i][v] = 选手i获得v分的次数
counts = [[0] * 11 for _ in range(N)]
for i in range(N):
    for j in range(M):
        counts[i][scores[j][i]] += 1  # scores[j][i]表示的是下标

# 排序：总分降序，同分依次比较10分、9分...
def sort_key(i):
    key = [total[i]]  # 第一优先级, 总分
    for v in range(10, 0, -1):
        key.append(counts[i][v])  # 后序优先级
    return key

players = sorted(range(N), key=sort_key, reverse=True)  # 对选手编号进行排序

print(','.join(str(p + 1) for p in players[:3]))