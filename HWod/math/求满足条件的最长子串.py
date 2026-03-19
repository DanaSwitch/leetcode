# 读取一行输入
input_str = input()
idx = [-1]

# 收集所有字母的索引
for i, c in enumerate(input_str):
    if c.isalpha():
        idx.append(i)
idx.append(len(input_str))

# 全是字母或全是非字母
if len(idx) == 2 or len(idx) == len(input_str) + 2:
    print(-1)
else:
    res = 0
    # 计算两两字母之间的最长非字母子串
    for i in range(1, len(idx) - 1):
        left = idx[i - 1] + 1
        right = idx[i + 1] - 1
        res = max(res, right - left + 1)
    print(res)
