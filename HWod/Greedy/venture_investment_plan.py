"""
思路: 这题的风险等级是争对单个产品的
"""
def solve():
    lines = list(map(int, input().strip().split()))
    if not lines:
        return
    m, n, x, y = lines[0], lines[1], lines[2], lines[3]   # 总钱, 总数, 风险, 回报
    nums = []
    for _ in range(n):
        e, r = map(int, input().strip().split())
        if r > x:  # 风险高于x的直接跳
            continue
        nums.append(e)
    
    nums.sort(reverse = True)
    remain = m  # 剩余的钱
    result = 0  # 预期收益

    for i in nums:
        if remain <= 0:
            break
        cost = min(y, remain)
        result += cost * i
        remain -= cost

    print(round(result/100))

if __name__ == "__main__":
    solve()