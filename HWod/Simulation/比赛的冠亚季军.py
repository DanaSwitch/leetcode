from collections import deque


def solve():
    strengths = list(map(int, input().split()))
    n = len(strengths)
    athletes = list(range(n))

    def duel_round(players):
        winners, losers = [], []
        i = 0
        while i + 1 < len(players):
            a, b = players[i], players[i + 1]
            # 关键修复：明确比较实力，相等时 id 小的赢
            if strengths[a] > strengths[b] or \
               (strengths[a] == strengths[b] and a < b):
                winners.append(a)
                losers.append(b)
            else:
                winners.append(b)
                losers.append(a)
            i += 2
        if len(players) % 2 == 1:
            winners.append(players[-1])
        return winners, losers

    duel_result = deque()

    winners, losers = duel_round(athletes)
    duel_result.appendleft(losers)
    duel_result.appendleft(winners)

    while len(duel_result[0]) > 1:
        winners, losers = duel_round(duel_result[0])
        duel_result.appendleft(losers)
        duel_result.appendleft(winners)
        while len(duel_result) > 4:
            duel_result.pop()

    first = duel_result[0][0]
    second = duel_result[1][0]
    # 半决赛所有输家中取最强（实力相同取 id 最小）
    third = max(duel_result[3], key=lambda x: (strengths[x], -x))

    print(first, second, third)


solve()