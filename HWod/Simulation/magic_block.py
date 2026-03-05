def steps_to_zero(h):
    """
    单个积木堆从高度h降到0, 独立操作需要几次魔法
    例如: h=9 → 4 → 2 → 1 → 0, 需要4次
    """
    count = 0
    while h > 0:
        h //= 2
        count += 1
    return count


def shared_steps(a, b):
    """
    计算相邻两堆可以共享的魔法次数
    思路: 让较大的数不断除以2, 直到两数相遇
    相遇之后到0的步数, 就是可以一起施魔法的次数
    """
    if a == 0 or b == 0:
        return 0

    # 不断让较大的数减半，直到两数相等
    while a != b:
        if a > b:
            a //= 2
        else:
            b //= 2

    # 此时 a == b，从这里到0还需要几步
    count = 0
    while a > 0:
        a //= 2
        count += 1
    return count


# 读取输入
n = int(input())
heights = list(map(int, input().split()))

# 第一步：计算所有堆单独操作的总次数
total = sum(steps_to_zero(h) for h in heights)

# 第二步：减去相邻堆可以共享的次数
for i in range(n - 1):
    total -= shared_steps(heights[i], heights[i + 1])

print(total)