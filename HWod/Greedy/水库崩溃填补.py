# 将字符串按逗号切割并转成整数列表
def split_to_int_list(s):
    return list(map(int, s.split(',')))

import sys

data = sys.stdin.read().strip().split()
# data = ["3","8,0,8","2","7,6"]

n = int(data[0])
str1 = data[1]
m = int(data[2])
str2 = data[3]

hight = split_to_int_list(str1)
woods = split_to_int_list(str2)

# 记录需要填充的溃口及高度
need = []
for i in range(1, n - 1):
    diff = hight[0] - hight[i]
    if diff > 0:
        need.append(diff)

# 统计木材数量（木材高度 ≤ 15）
count = [0] * 17
for h in woods:
    count[h] += 1

total = 0

for needH in need:
    flag = False

    # 优先使用 ≥ needH 的木材
    for j in range(needH, 17):
        if count[j] > 0:
            count[j] -= 1
            total += j
            flag = True
            break

    # 使用 < needH 的最大木材
    if not flag:
        for j in range(needH - 1, 0, -1):
            if count[j] > 0:
                count[j] -= 1
                total += j
                flag = True
                break

    if not flag:
        break

print(total)
