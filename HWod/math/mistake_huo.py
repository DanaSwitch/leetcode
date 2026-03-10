"""
思路: 0 与 1 互换会导致结果改变
total_0*one_1 + total_1*one_0 - one_0*one_1(重复了)
"""

n = int(input())
line_one = input()
line_two = input()

def solve():
    one_0 = 0  # 第二个中0对应第一个0的数量
    one_1 = 0  # 第二个中0对应第一个1的数量
    total_0 = 0  #第一个中0的总数
    total_1 = 0  #第以个中1的总数

    for i in range(n):
        if line_one[i] == '0':
            total_0 += 1
            if line_two[i] == '0':
                one_0 += 1
        else:
            total_1 += 1
            if line_two[i] == '0':
                one_1 += 1

    return (total_0*one_1 + total_1*one_0 - one_0*one_1)

print(solve())