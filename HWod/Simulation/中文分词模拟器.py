import re

line1 = input().strip()
line2 = input().strip()

# 将词库字符串按逗号分割, 存入集合（set）
# 使用集合的目的: 查找某个词是否存在时, 时间复杂度为 O(1)，比列表更高效
dictionary = set(line2.split(','))

# 按标点符号（逗号、分号、句号）对原字符串进行断句
segments = re.split(r'[,;.]', line1)
result = []  # 存储最终分词结果

for seg in segments:  # 单个分词
    if not seg:
        continue
    i = 0
    while i < len(seg):
        best = None  # 记录当前位置找到的最长匹配词
        # j 从字符串末尾向 i+1 递减, 先试最长子串, 再试较短的（保证最长匹配）
        for j in range(len(seg), i, -1):
            if seg[i:j] in dictionary:
                best = seg[i:j]  # 找到第一个（最长的）匹配词，立即停止
                break
        if best:
            # 匹配成功: 将该词加入结果, 指针跳过已匹配的部分
            result.append(best)
            i += len(best)
        else:
            # 匹配失败, 则将单个字符直接作为分词结果输出（兜底处理）
            result.append(seg[i])
            i += 1  # 指针前移一位, 继续处理下一个字符

print(','.join(result))