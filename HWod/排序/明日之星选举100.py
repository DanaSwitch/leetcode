from collections import defaultdict

M = int(input())  # 选票数量
vote = []
for _ in range(M):
    row = input().split(',')  # split()会自动分隔列表
    vote.append(row)

agree = defaultdict(int)
disagree = defaultdict(int)
all_names = set()

for row in vote:
    supporter = row[0]
    agree[supporter] += 1
    all_names.add(supporter)
    
    if len(row) == 2:  # 反对票可选, 有逗号才处理
        opponent = row[1]
        disagree[opponent] += 1
        all_names.add(opponent)

N = int(input())  # 最终当选人数

# 排序规则：赞成票降序 → 反对票升序 → 姓名字典序升序
sorted_names = sorted(
    all_names,
    key=lambda name: (-agree[name], disagree[name], name)
)

print(','.join(sorted_names[:N]))