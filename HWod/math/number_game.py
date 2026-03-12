"""
思路: 记录已经出现过的 remainder = cur_sum % m 
      remainder == 0 or remainder在之前出现过
"""
import sys

for lines in sys.stdin:
    n, m = map(int, lines.split())  # n张牌, 牌上数字m
    cards = list(map(int, sys.stdin.readline().strip().split()))

    remainder_list = [False] * m

    total = 0
    find = False  
    for card in cards:
        total += card
        remainder = total % m
        if remainder_list[remainder] or remainder == 0:
            find = True
            break
        remainder_list[remainder] = True
    print(1 if find else 0)