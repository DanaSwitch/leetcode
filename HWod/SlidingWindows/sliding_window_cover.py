import sys

def find_redundant_cover():
    input_data = sys.stdin.read().split()
    if len(input_data) < 3:
        return
    
    s1 = input_data[0]
    s2 = input_data[1]
    k = int(input_data[2])
    
    n1, n2 = len(s1), len(s2)
    window_len = n1 + k
    
    # 基础边界检查
    if n2 < window_len:
        print("-1")
        return

    # 预处理：将字符转换为 0-25 的整数，极大提升循环效率
    s1_ids = [ord(c) - ord('a') for c in s1]
    s2_ids = [ord(c) - ord('a') for c in s2]

    # 统计 s1 字母个数
    s1_count = [0] * 26
    for idx in s1_ids:
        s1_count[idx] += 1
    
    window_count = [0] * 26  # 窗口内字母个数
    s1_chars_needed = n1  # 还需要匹配的字符总数
    
    # 滑动窗口逻辑, 题目要求找满足条件的最左侧下标, 找到的第一个就是最左侧的
    left = 0
    for right in range(n2):
        # 1. 进窗：右边界字符
        r_char = s2_ids[right]
        window_count[r_char] += 1
        
        # 如果这个字符是 s1 需要的，且窗口内还没攒够，则有效匹配数 +1
        # 注意：这里我们反过来思考，用“有效匹配”达到 n1 作为成功标志
        if window_count[r_char] <= s1_count[r_char]:  # 默认都比较r_char这个字符
            s1_chars_needed -= 1
        
        # 2. 缩窗：当窗口长度超过 n1 + k 时，移动左边界
        if right - left + 1 > window_len:
            l_char = s2_ids[left]
            # 如果移出的字符是有效匹配的一部分，则缺口增加
            if window_count[l_char] <= s1_count[l_char]:
                s1_chars_needed += 1
            window_count[l_char] -= 1
            left += 1
            
        # 3. 检查：如果缺口为 0，说明当前窗口完全覆盖了 s1
        if s1_chars_needed == 0:
            print(left)
            return

    print("-1")

if __name__ == "__main__":
    find_redundant_cover()