n = int(input())
target_name = input()
all_files = []
for _ in range(n):
    row = input().split()
    all_files.append(row)

def parse_file(file):
    name, time = file[0], int(file[1])
    striped_name = name.lstrip('-')
    diff = len(name) - len(striped_name)
    level = diff//4
    return level, striped_name, time

# 存入文件
stripped_files = []
for file in all_files:
    level, striped_name, time = parse_file(file)
    stripped_files.append([level, striped_name, time])

# 找到目标文件下标
target_id = None
target_level = None
for i in range(n):
    level, name, time = stripped_files[i]
    if name == target_name and time == -1:  # 是文件
        target_id = i
        target_level = level

# ✅ 加上这个判断
if target_id is None:
    print("No file")
    exit()

# 找出目标文件下的子文件
result = []  # (名字, 时间戳)
for j in range(target_id+1, n):
    level, name, time = stripped_files[j]
    if level <= target_level:
        break
    else:
        if time != -1:  # 是文件
            result.append((name, time))

if result:
    result.sort(key= lambda x: x[1])
    for name, time in result:
        print(f"{name} {time}")
else:
    print("No file")