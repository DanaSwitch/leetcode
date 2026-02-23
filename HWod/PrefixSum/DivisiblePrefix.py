import sys

def solve():  
    input_data = sys.stdin.read().split()
    iterator = iter(input_data)

    n = int(next(iterator))
    m = int(next(iterator))

    cards = [int(x) for x in iterator]
    # remainder_set 记录已经出现过的余数
    # 初始放入 0，是因为如果某个前缀和直接被 m 整除，余数就是 0
    remainder_seen = {0}
    current_sum = 0
    found = False

    for card in cards:
        current_sum += card
        remainder = current_sum % m
        
        if remainder in remainder_seen:
            found = True
            break
        
        remainder_seen.add(remainder)

    if found:
        print("1")
    else:
        print("0")

if __name__ == "__main__":
    solve()