import sys

input_data = sys.stdin.read().split()
if len(input_data) < 2:
    exit()
s1 = input_data[0]
s2 = input_data[1]

# 辅助函数: 将压缩字符串解析成 [数量, 字符] 的列表
# 例如 "3A12B" -> [[3, 'A'], [12, 'B']]
def parse_strs(s):
    result = []
    num_str = ""
    for char in s:
        if char.isdigit():
            num_str += char  # 拼接数字
        else:
            result.append([int(num_str), char]) # 遇到字母, 保存数字和字母
            num_str = ""     # 重置数字字符串
    return result
    
p1 = parse_strs(s1)
p2 = parse_strs(s2)

diff_count = 0  # 误码数量
total_count = 0 # 总数量

i, j = 0, 0     # 双指针，分别指向 p1 和 p2 的当前块

while i < len(p1) and j < len(p2):
    cnt1, char1 = p1[i]
    cnt2, char2 = p2[j]
    # 取两个当前块中较小的数量，作为本次可以共同处理的长度
    process_len = min(cnt1, cnt2)
    # 如果字符不同, 累加到误码数中
    # 公共字段不同
    if char1 != char2:
        diff_count += process_len
    total_count += process_len
    # 将已处理的数量从块中扣除
    p1[i][0] -= process_len
    p2[j][0] -= process_len
    # 如果当前块处理完了（数量归零）, 指针就移动到下一个块
    if p1[i][0] == 0:
        i += 1
    if p2[j][0] == 0:
        j += 1
# 按题目要求的格式输出，注意不需要化简分数
print(f"{diff_count}/{total_count}")
