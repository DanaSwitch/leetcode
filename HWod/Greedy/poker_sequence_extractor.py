import sys

def solve():
    # 使用不同的变量命名风格
    raw_input = sys.stdin.readline().strip()
    
    # ranj_map : 映射
    # 将字符牌转化为对应的整数权重, c是键, i是值, enumerate会自动将i生成为整数
    rank_map = {c: i for i, c in enumerate(["3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A", "2"])}
    # 给予'2'特殊权重，确保其不会被顺子逻辑捕获
    rank_map["2"] = 999

    all_cards = raw_input.split()
    all_cards.sort(key=lambda item: rank_map.get(item, 0))  # 根据映射的权重排序

    # grouped 存放连在一起的牌
    grouped = [[all_cards[0]]]

    # 核心扫描逻辑
    for i in range(1, len(all_cards)):
        current_card = all_cards[i]
        is_extended = False
        
        # 尝试连接现有顺子
        for sequence in grouped:
            if rank_map[current_card] - rank_map[sequence[-1]] == 1:  # 新牌比最后一个牌大1
                sequence.append(current_card)  # 在当前列表添加
                is_extended = True
                break
        
        # 若无法连接，则作为新序列的起点
        if not is_extended:
            grouped.append([current_card])  # 加入新列表

    # 结果过滤与展示
    is_found = False
    for sequence in grouped:
        if len(sequence) >= 5:
            print(" ".join(sequence))  # sequance列表里面是字符
            is_found = True

    if not is_found:
        print("No")

if __name__ == "__main__":
    solve()