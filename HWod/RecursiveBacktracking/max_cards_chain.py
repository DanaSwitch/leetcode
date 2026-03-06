def solve():
    nums = list(map(int, input().split()))
    colors = input().split()
    n = len(nums)
    cards = list(zip(nums, colors))  # [(数字, 颜色), ...]
    
    # 记录所有记录中的最高记录
    best = [0]  # 使用列表是为了能够在嵌套循环中修改它
    
    def backtrack(last_card, used, count):
        best[0] = max(best[0], count)
        
        for i in range(n):
            if used[i]:
                continue
            num, color = cards[i]
            # 第一张随便打, 或者颜色/数字匹配上一张
            if last_card is None or num == last_card[0] or color == last_card[1]:
                used[i] = True
                # count + 1, 进入下一轮递归
                backtrack(cards[i], used, count + 1)
                used[i] = False  # 回溯
    
    backtrack(None, [False] * n, 0)  # 在这里创建 used = [False] * n
    print(best[0])

solve()