"""
思路: 注意最后AB右侧相等, 是判断A_line1[a_left] < B_line2[b_right]: 再田忌赛马
"""
n = int(input())

A_line1 = list(map(int, input().strip().split()))
B_line2 = list(map(int, input().strip().split()))

A_line1.sort()
B_line2.sort()

a_left, a_right = 0, n-1
b_left, b_right = 0, n-1
count = 0  # 赢的次数
# 田忌赛马
while a_right >= a_left:
    if A_line1[a_right] > B_line2[b_right]:
        count += 1
        a_right -= 1
        b_right -= 1
    # 让A小的抵消B大的
    elif A_line1[a_right] < B_line2[b_right]:
        count -= 1
        a_left += 1
        b_right -= 1
    else:  # A与B最大的相等
        # A[2,4],B[3,4] 与 A[3,4],B[2,4]
        # A最小的比B最小的大
        if A_line1[a_left] > B_line2[b_left]:
            count += 1
            a_left += 1
            b_left += 1
        else:
            if A_line1[a_left] < B_line2[b_right]:
                count -= 1
            a_left += 1
            b_right -= 1

print(count)