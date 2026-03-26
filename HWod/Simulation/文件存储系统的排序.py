def solve():
    n = int(input())
    target_name = input()
    messages = []
    for _ in range(n):
        messages.append(input())

    def parse_file(line):
        tmp = line.lstrip('-')
        level = (len(line)-len(tmp))//4
        parts = tmp.strip().split()
        name = parts[0]
        time = int(parts[1])
        return level, name, time

    all_files = [parse_file(data) for data in messages]

    target_id = None
    target_level = None
    # 找出目标文件的位置
    for i, (level, name, time) in enumerate(all_files):
        if name == target_name and time == -1:
            target_level = level
            target_id = i
            break

    if target_id is None:
        print(-1)
        return
    
    # 收集目标文件夹下的所有文件
    files = []
    for i in range(target_id+1, len(all_files)):
        level, name, time = all_files[i]
        if level <= target_level:
            break  # 跳出目标文件层级了
        if time != -1:  # 是文件
            files.append((name, time))
        
    if not files:
        print(-1)
        return
    
    # 按照文件时间戳排序
    files.sort(key=lambda x: x[1])
    for name, time in files:
        print(f"{name} {time}")

if __name__ == "__main__":
    solve()