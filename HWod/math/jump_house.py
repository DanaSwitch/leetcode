"""
思路: 将两轮循环变成一轮, 本来是找steps[i] + steps[j] = target
      转变成遍历steps[j], 查找前面有没有出现过 target - steps[j]
      没有就用哈希表记录下来, 注意键存储的是数, 值才是索引
"""

def solve(steps, count):
    memo = {}  # {值: 索引}
    min_index_sum = float('inf')
    result = None

    for j, num in enumerate(steps):
        target = count - num
        if target in memo:
            i = memo[target]
            if i + j < min_index_sum:
                min_index_sum = i + j
                result = [steps[i], num]
        if num not in memo:
            memo[num] = j
    return result

if __name__ == "__main__":
    steps = list(map(int, input().strip()[1:-1].split(',')))
    count = int(input().strip())
    print(solve(steps, count))