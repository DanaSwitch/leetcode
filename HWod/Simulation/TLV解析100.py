raw_str = input().strip()
n = int(input())

query_tag = []
for _ in range(n):
    tmp = int(input())
    query_tag.append(tmp)

# 解析
tlv_map = {}  # {tag:(length, value_offset)}

i = 0  # 当前字节偏移
while True:
    # 必须有 tag + length
    if (i+2) * 2  > len(raw_str):
        break

    # 解析
    tag = int(raw_str[i*2: i*2+2], 16)
    length = int(raw_str[(i+1)*2: (i+1)*2+2], 16)
    value_offset = i + 2

    # 检查value是否完整
    if (i+2+length)*2 > len(raw_str):
        break

    tlv_map[tag] = (length, value_offset)
    i += 2 + length  # 移动到下一组TLV

for query in query_tag:
    if query in tlv_map:
        length1, value_offset1 = tlv_map[query]
        print(f"{length1} {value_offset1}")
    else:
        print("0 0")