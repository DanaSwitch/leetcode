from itertools import combinations

def solve():
    # 使用切片方式解析字符串 [0,1,2] -> [0, 1, 2]
    line1 = input().strip()
    if line1 == "[]":
        lines = []
    else:
        lines = list(map(int, line1[1:-1].split(',')))
        
    num = int(input().strip())  # 申请的处理器数量
    
    # 链路划分逻辑
    link1 = sorted([x for x in lines if 0 <= x <= 3])
    link2 = sorted([x for x in lines if 4 <= x <= 7])
    
    if num == 8:
        return [sorted(lines)] if len(lines) == 8 else []

    # 优先级映射
    priority_map = {
        1: {1: 0, 3: 1, 2: 2, 4: 3},
        2: {2: 0, 4: 1, 3: 2},
        4: {4: 0}
    }
    pmap = priority_map.get(num, {})  # 返回num对应的优先级队列
    
    candidates = []
    if len(link1) >= num:
        candidates.append((pmap.get(len(link1), 99), link1))
    if len(link2) >= num:
        candidates.append((pmap.get(len(link2), 99), link2))
        # [(1, [link1的详细数据]), (0, [link2的详细数据])]
    
    if not candidates:
        return []
    
    best_priority = min(c[0] for c in candidates)  # 选优先级更小的
    best_links = [c[1] for c in candidates if c[0] == best_priority]
    
    result = []
    for link in best_links:
        for combo in combinations(link, num):
            result.append(list(combo))
            
    return result

print(solve())