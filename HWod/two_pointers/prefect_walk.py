import collections

def min_replace_length():
    # 读取输入并去除首尾空格
    s = input().strip()

    n = len(s)
    # 目标数量：每个字符应该出现的次数
    target = n // 4
    # 统计当前字符串中各字符的数量
    # Counter 会生成类似 {'A': 2, 'S': 1, ...} 的字典
    count = collections.Counter(s)
    # 检查是否已经是完美走位
    if all(count[c] == target for c in "WASD"):
        print(0)
        return
    min_len = n  # 初始化最小长度为最大可能值
    left = 0     # 滑动窗口左指针, 不断缩小待修改的最小长度
    # right 为滑动窗口右指针，从左向右遍历
    for right in range(n):
        # 将 s[right] 加入窗口，意味着它被标记为"待替换"
        # 所以我们在剩余字符计数中减去它
        count[s[right]] -= 1

        # 检查条件：如果窗口外的所有字符数量都 <= target
        # 说明我们可以通过修改窗口内的字符来达到平衡
        while all(count[c] <= target for c in "WASD"):
            # 更新最小长度
            current_len = right - left + 1
            min_len = min(min_len, current_len)

            # 尝试缩小窗口: 将 s[left] 移出窗口
            # 意味着它不再被替换, 要加回到剩余字符计数中
            # 先更新状态, 再移动指针
            count[s[left]] += 1
            left += 1

    print(min_len)


if __name__ == "__main__":
    min_replace_length()