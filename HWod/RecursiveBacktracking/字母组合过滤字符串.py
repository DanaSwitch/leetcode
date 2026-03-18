# 定义映射关系
char_map = ["abc", "def", "ghi", "jkl", "mno", "pqr", "st", "uv", "wx", "yz"]
filter_set = set()

# 判断是否包含所有过滤字符
def is_contains_all_filter_chars(used):
    return any(x not in used for x in filter_set)

# 递归回溯
def dfs(letters, index, path, res, used):
    if index == len(letters):
        if is_contains_all_filter_chars(used):
            res.append("".join(path) + ",")
        return

    # 遍历当前数字对应的字母
    for c in letters[index]:
        path.append(c)
        used.add(c)
        dfs(letters, index + 1, path, res, used)
        path.pop()
        used.remove(c)

# 处理输入
digits = input().strip()
filter_chars = input().strip()

filter_set = set(filter_chars)
letters = [char_map[int(d)] for d in digits]

# 开始递归
res = []
dfs(letters, 0, [], res, set())

# 输出结果
print("".join(res))