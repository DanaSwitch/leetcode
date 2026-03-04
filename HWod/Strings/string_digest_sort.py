def get_digest():
    # 1. 预处理：清洗数据
    raw_s = input().lower()  # 转化为小写
    s = "".join(c for c in raw_s if 'a' <= c <= 'z')  # 挑出小写字母黏在一起
    if not s: return

    # 2. 统计总频次
    total_count = {}
    for char in s:
        total_count[char] = total_count.get(char, 0) + 1

    # 3. 双指针扫描分组
    res = []
    i = 0
    while i < len(s):
        j = i
        # 寻找连续相同字符的末尾（j 指向第一个不同的字符）
        while j < len(s) and s[j] == s[i]:
            j += 1  # 不连续就退出 while 循环
        
        char = s[i]
        length = j - i # 连续出现的长度
        
        # 核心逻辑：更新该字符的总频次，减去当前已经看过的部分
        total_count[char] -= length
        
        if length > 1:
            res.append([char, length])
        else:
            # 非连续, 计算该字母后面的次数
            res.append([char, total_count[char]])
        
        # 将 i 移到下一个不同字符的位置
        i = j

    # 4. 先按数字倒序排列, 后按照字母正序排列
    res.sort(key=lambda x: (-x[1], x[0]))
    print("".join(f"{x[0]}{x[1]}" for x in res))

get_digest()