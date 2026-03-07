def solve():
    nums = sorted(list(map(int, input().split())))
    max_length = nums[-1]
    # 总长度
    total_length = sum(nums)

    possible = True
    # 遍历可能的层长
    for L in range(max_length, total_length + 1):
        if total_length % L != 0:
            continue
        left, right = 0, len(nums)-1
        while left <= right:
            if nums[right] == L:  # 单个配对
                right -= 1
            elif nums[left] + nums[right] == L:  # 两两配对
                left += 1
                right -= 1
            else:  # 无法配对
                possible = False
                break  # 结束while循环
    
        if possible:  # 打印第一个L
            print(total_length // L)
            return
    print(-1)  # 遍历整个for循环都没找到就打印-1
if __name__ == "__main__":
    solve()                           