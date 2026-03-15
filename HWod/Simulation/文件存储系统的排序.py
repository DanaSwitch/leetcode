def solve():
    n = int(input())
    target = input().strip()  # 目标文件夹
    
    lines = []
    for _ in range(n):
        lines.append(input())
    
    # 解析每行：层级、名称、时间戳
    parsed = []
    for line in lines:
        stripped = line.lstrip('-')  # 只删除左边的'-'
        _count = len(line) - len(stripped)
        level = _count // 4          # 每4个'-'表示一层
        parts = stripped.split()
        name = parts[0]
        time = int(parts[1])
        parsed.append((level, name, time))
    
    # 找目标文件夹的位置
    target_idx = -1
    for i, (level, name, time) in enumerate(parsed):
        if name == target and time == -1:
            target_idx = i
            break
    
    if target_idx == -1:  # 没找到
        print("No file")
        return
    
    target_level = parsed[target_idx][0]
    
    # 收集目标文件夹下的所有文件（层级更深的所有非文件夹条目）
    files = []
    i = target_idx + 1
    while i < len(parsed):
        level, name, time = parsed[i]
        if level <= target_level:    # 回到同级或更高，停止
            break
        if time != -1:                 # 不是文件夹，是文件
            files.append((time, name))
        i += 1
    
    if not files:
        print("No file")
        return
    
    files.sort()                     # 按时间戳升序排序
    for time, name in files:
        print(f"{name} {time}")

solve()