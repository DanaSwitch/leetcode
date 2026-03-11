n = int(input())
records = [input().strip() for _ in range(n)]

lines = []
for r in records:
    a, b, c, d, e = r.split(',')
    lines.append((a, int(b), int(c), d, e))

abnormal = set()  # 异常记录

for i, (id1, t1, d1, act1, reg1) in enumerate(lines):
    if act1 != reg1:
        abnormal.add(i)
    # 不写else是使用set()会去重
    for j, (id2, t2, d2, act2, reg2) in enumerate(lines):
        if i != j and id1 == id2:  # 相同工号的不同记录
            if abs(t1 - t2) < 60 and abs(d1 - d2) > 5:
                abnormal.add(i)
                abnormal.add(j)  # j在i的后面

result = [records[i] for i in range(n) if i in abnormal]
print(';'.join(result) if result else 'null')