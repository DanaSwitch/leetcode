"""
思路: 注意本题求的是对手可能出现最长顺子, 不是自己
"""
def solve():
    hand_str = input().strip()
    played_str = input().strip()
    
    # 顺子有效牌型（3到A，共12种）
    ranks = ['3','4','5','6','7','8','9','10','J','Q','K','A']
    rank_idx = {r: i for i, r in enumerate(ranks)}
    
    hand_count   = [0] * 12
    played_count = [0] * 12
    
    for c in hand_str.split('-'):
        if c in rank_idx:
            hand_count[rank_idx[c]] += 1

    for c in played_str.split('-'):
        if c in rank_idx:
            played_count[rank_idx[c]] += 1

    # 对手每种牌的可用数量
    available = [4 - hand_count[i] - played_count[i] for i in range(12)]

    best_len = 0
    best_end = -1

    # 双指针扫描, 找出所有连续可用段
    i = 0
    while i < 12:
        if available[i] >= 1:  # 遇到可用的牌
            j = i
            while j < 12 and available[j] >= 1:
                j += 1
            length = j - i  # 遇到断点退出, 记录此时长度
            # 长度≥5才是合法顺子, 同长度取更靠后（牌面更大）的
            if length >= 5:
                # 注意j 要减1
                # 长度更长, 或者牌面更大才更新
                if length > best_len or (length == best_len and j - 1 > best_end):
                    best_len = length
                    best_end = j - 1
            i = j  # 跳过这一段, 继续向下找
        else:
            i += 1

    if best_len == 0:
        print("NO-CHAIN")
    else:
        best_start = best_end - best_len + 1
        print('-'.join(ranks[best_start : best_end + 1]))

solve()