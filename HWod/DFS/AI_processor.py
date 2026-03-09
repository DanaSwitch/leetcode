def parse_array(line):
    """手动解析形如 "[0, 1, 4, 5, 6, 7]" 的字符串"""
    line = line.strip().strip('[]')
    if not line:
        return []
    return [int(x.strip()) for x in line.split(',')]


def get_combinations(arr, num):
    """回溯法实现组合"""
    result = []
    combo = []

    def backtrack(start):
        if len(combo) == num:
            result.append(combo[:])
            return
        remaining_needed = num - len(combo)
        for i in range(start, len(arr) - remaining_needed + 1):
            combo.append(arr[i])
            backtrack(i + 1)
            combo.pop()

    backtrack(0)
    return result


def get_processor_combinations(array, num):
    chain0 = sorted([x for x in array if 0 <= x <= 3])
    chain1 = sorted([x for x in array if 4 <= x <= 7])
    chains = [chain0, chain1]

    if num == 8:
        if len(array) == 8:
            return [sorted(array)]
        return []

    priority_map = {
        1: [1, 3, 2, 4],
        2: [2, 4, 3],
        4: [4],
    }

    for target_size in priority_map[num]:
        result = []
        for chain in chains:
            if len(chain) == target_size:
                for combo in get_combinations(chain, num):
                    result.append(combo)
        if result:
            return result

    return []


line1 = input().strip()
num = int(input().strip())
array = parse_array(line1)

result = get_processor_combinations(array, num)
print(result)