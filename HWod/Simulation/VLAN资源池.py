def process_vlan_pool(vlan_pool_input, need_vlan_id):
    # 按 "," 分割并处理为区间
    ranges = []
    for part in vlan_pool_input.split(","):
        if "-" in part:
            bounds = list(map(int, part.split("-")))
            ranges.append(bounds)
        else:
            value = int(part)
            ranges.append([value, value])

    # 排序区间
    ranges.sort(key=lambda x: x[0])

    # 合并和处理区间
    result = []
    for start, end in ranges:
        if need_vlan_id >= start and need_vlan_id <= end:
            # 左区间的右边界
            left_section_right = need_vlan_id - 1
            # 右区间的左边界
            right_section_left = need_vlan_id + 1
            if left_section_right > start:
                result.append(f"{start}-{need_vlan_id - 1}")
            elif left_section_right == start:
                result.append(f"{start}")
                
            if right_section_left < end:
                result.append(f"{need_vlan_id + 1}-{end}")
            elif right_section_left == end:
                result.append(f"{end}")
        else:
            result.append(f"{start}-{end}" if start != end else str(start))

    # 输出结果
    return ",".join(result)


if __name__ == "__main__":
    vlan_pool_input = input()
    need_vlan_id = int(input())
    output = process_vlan_pool(vlan_pool_input, need_vlan_id)
    print(output)
