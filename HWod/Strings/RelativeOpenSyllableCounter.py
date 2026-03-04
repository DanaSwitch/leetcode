import re

def solve():
    # 1. 获取输入并分词
    line = input().strip()
    if not line:
        return 0
    words = line.split()
    
    # 2. 预编译正则表达式（效率最高）
    # 辅音(除aeiou): [b-df-hj-np-tv-z]
    # 元音: [aeiou]
    # 辅音(除aeiour): [b-df-hj-np-qstv-z]
    # 结尾: e
    pattern = re.compile(r'[b-df-hj-np-tv-z][aeiou][b-df-hj-np-qstv-z]e')
    non_letter = re.compile(r'[^a-z]') # 匹配任何非小写字母的字符
    
    total_count = 0
    
    for word in words:
        # 3. 核心逻辑：判断是否含有非字母
        # 如果没有非字母（即全小写），则翻转单词
        if not non_letter.search(word):  # 没有搜到非字母的单词, 则需要反转
            word = word[::-1]
        
        # 4. 滑动窗口统计（因为题目说可以重叠）
        # 比如单词 "abeke"，长度为5，需要检查 "abek" 和 "beke"
        for i in range(len(word) - 3):
            sub_str = word[i:i+4]
            # 使用 fullmatch 确保这4个字符完全符合开音节结构
            if pattern.fullmatch(sub_str):
                total_count += 1
                
    return total_count

# 执行并打印结果
print(solve())