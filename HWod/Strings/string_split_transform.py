k = int(input())
s = input()

# 1. 拆分：把第一个子串拿出来，剩下的拼成一个长串
parts = s.split('-')
prefix = parts[0]
others = "".join(parts[1:]) 

# 2. 分段转换：每 K 个字符处理一次
new_parts = []
for i in range(0, len(others), k):
    # 取出当前这 K 个字符
    sub = others[i : i + k]
    
    # 数一下大小写字母各有多少个
    upper_cnt = 0
    lower_cnt = 0
    for char in sub:
        if char.isupper(): upper_cnt += 1
        if char.islower(): lower_cnt += 1
    
    # 根据数量多少决定转换方式
    if upper_cnt > lower_cnt:
        new_parts.append(sub.upper())
    elif lower_cnt > upper_cnt:
        new_parts.append(sub.lower())
    else:
        new_parts.append(sub)

# 3. 拼接：把开头和处理后的各段连起来
result = prefix + "-" + "-".join(new_parts)
print(result)