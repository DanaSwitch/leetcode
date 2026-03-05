import sys

def solve():
    # --- 1. 获取输入 ---
    # sys.stdin.readline() 读取一行，strip() 去掉两端的空格或换行
    my_input = sys.stdin.readline().strip()
    used_input = sys.stdin.readline().strip()

    # --- 2. 初始化一副牌的数量 (每种点数初始有4张) ---
    # 我们只关心能做顺子的 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A
    cards_order = ["3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    counts = {card: 4 for card in cards_order}  # 字典, 每个牌四张

    # --- 3. 扣掉已经出现的牌, 就是对手的牌 ---
    # 处理我手里的牌
    if my_input:
        for card in my_input.split("-"):
            if card in counts:
                counts[card] -= 1
    # 处理已经出过的牌
    if used_input:
        for card in used_input.split("-"):
            if card in counts:
                counts[card] -= 1

    # --- 4. 寻找最长连续序列 ---
    # 将 counts 转换成一个 0/1 序列，1表示对手手里还有这张牌
    has_card = [1 if counts[card] > 0 else 0 for card in cards_order]  # 记录对手的牌
    
    # 

    max_len = 0  # 顺子最大长度
    best_straight = []
    """滑动窗口"""
    # 外层循环：尝试每一个起点 i
    for i in range(len(has_card)):
        # 内层循环：从起点 i 开始往后数，看能连多长
        if has_card[i] == 1:
            current_straight = []
            for j in range(i, len(has_card)):
                if has_card[j] == 1:
                    current_straight.append(cards_order[j])
                    
                    # 检查是否比目前找到的更长 (或者长度一样但牌面更大)
                    # 注意：因为我们是从左往右找，同长度时，后面的牌面一定更大
                    if len(current_straight) >= 5:
                        if len(current_straight) >= max_len:
                            max_len = len(current_straight)
                            best_straight = list(current_straight)
                else:
                    # 断开了，跳出内层循环
                    break

    # --- 5. 输出结果 ---
    if not best_straight:
        print("NO-CHAIN")
    else:
        print("-".join(best_straight))

if __name__ == "__main__":
    solve()