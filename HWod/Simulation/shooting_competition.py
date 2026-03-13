from collections import defaultdict

n = int(input())
id = input().split(',')
sorce = input().split(',')

id_sorce_map = defaultdict(list)

for i in range(n):
    # 对于id和成绩, 记得转为int类型
    id_sorce_map[int(id[i])].append(int(sorce[i]))  # 对字典里面的列表进行append

person = []

for _id, _sorce in id_sorce_map.items():
    if len(_sorce) < 3:
        continue
    _sorce.sort(reverse=True)
    total = sum(_sorce[:3])
    person.append([total, _id])

sorted_person = sorted(person, key= lambda x: (-x[0], -x[1]))
result = [p[1] for p in sorted_person] 

print(",".join(map(str, result)))