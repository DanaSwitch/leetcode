def dfs(nums, min_count, start, path, result):
    # 出口
    if len(path) >= min_count:
        result.append(path[:])
    
    for i in range(start, len(nums)):
        path.append(nums[i])
        dfs(nums, min_count, i + 1, path, result)
        path.pop()

nums = sorted(list(map(int, input().strip().split(','))))
min_count = int(input())
n = len(nums)

result = []  # 记录结果
dfs(nums, min_count, 0, [], result)

if not result:
    print("None")
else:
    for row in result:
        print(",".join(map(str, row)))