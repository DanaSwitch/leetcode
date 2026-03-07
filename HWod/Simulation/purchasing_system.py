import math
from collections import defaultdict

n = int(input())  # PR数量
PO1 = []  # 价格超过100
PO2 = defaultdict(lambda: [0, 0])  # 价格低于等于100

for _ in range(n):
    lines = list(map(int, input().split()))
    id, num, price, state = lines
    if state != 0:  # 审批没通过
        continue
    if price > 100:
        PO1.append((id, num, price))
    else:
        PO2[id][0] += num  # 相同商品的数量会合并在一起
        PO2[id][1] = price

PR = []

for id, num, price in PO1:
    PR.append((id, num, price))

for id, (total_num, price) in PO2.items():
    if total_num >= 100 and price < 100:  # 打9折
        price = math.ceil(price * 0.9)
    PR.append((id, total_num, price))

PR.sort(key = lambda x: (x[0], -x[1]))

for id, num, price in PR:
    print(id, num, price)