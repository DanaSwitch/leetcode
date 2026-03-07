import sys
from collections import defaultdict

def solve():
    # 读取所有输入
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    s = input_data[0]
    # 处理 k 可能在下一行或者同一行的情况
    if len(input_data) > 1:
        k = int(input_data[1])
    else:
        return

    n = len(s)
    
    # 状态变量
    cnt_digits = defaultdict(int) #键如果不存在, 默认当0处理
    satisfied_digits = 0  # 记录当前有多少种数字(0-9)已经出现
    
    c_low = 0   # l_k_low 窗口内的字母数量
    c_high = 0  # l_k_high 窗口内的字母数量
    
    # 三个左指针
    l_digit = 0
    l_k_low = 0
    l_k_high = 0
    
    ans = 0
    
    # 枚举右端点
    for right, char in enumerate(s):
        # --- 1. 更新计数器 ---
        
        # 更新数字计数
        if char.isdigit():
            if cnt_digits[char] == 0:
                satisfied_digits += 1
            cnt_digits[char] += 1
            
        # 更新字母计数（注意这里只是增加，收缩在后面）
        is_letter = char.islower()
        if is_letter:
            c_low += 1
            c_high += 1
            
        # --- 2. 维护 l_digit 指针 (数字约束) ---
        # 目标：找到最靠右的 l_digit，使得 s[l_digit...right] 包含所有数字
        # 只要当前窗口满足条件，且最左边的字符可以被丢弃（丢弃后依然满足），就右移 l_digit
        while satisfied_digits == 10:
            left_char = s[l_digit]
            can_remove = False
            
            if left_char.isdigit():
                # 如果这个数字出现次数多于1，说明删掉一个没事
                if cnt_digits[left_char] > 1:
                    can_remove = True
            else:
                # 如果是字母，对数字约束没影响，随便删
                can_remove = True
            
            if can_remove:
                if left_char.isdigit():
                    cnt_digits[left_char] -= 1
                l_digit += 1
            else:
                # 遇到了关键数字，不能再删了，停止
                break
        
        # 此时，对于数字约束，合法的 left 范围是 [0, l_digit] (闭区间)
        # 即 [0, l_digit + 1) (左闭右开)

        # --- 3. 维护 l_k_low 指针 (字母约束下限) ---
        # 目标：确保窗口内字母数 <= k。如果 > k，必须收缩。
        while c_low > k:
            if s[l_k_low].islower():
                c_low -= 1
            l_k_low += 1
            
        # --- 4. 维护 l_k_high 指针 (字母约束上限) ---
        # 目标：找到字母数变为 k-1 的临界点。
        # 也就是我们允许 left 向右移，直到窗口内的字母数量 < k 为止。
        while l_k_high <= right and c_high >= k:
            if s[l_k_high].islower():
                c_high -= 1
            l_k_high += 1
            
        # 此时，对于字母约束，合法的 left 范围是 [l_k_low, l_k_high)
        # 解释：l_k_low 是第一个满足 <= k 的位置。
        # l_k_high 是第一个满足 < k 的位置（因为循环是 >= k 时继续移，停下时即 < k）。
        # 所以在 [l_k_low, l_k_high-1] 之间的 left，字母数恰好是 k。

        # --- 5. 计算交集并累加答案 ---
        if satisfied_digits == 10:
            # 数字合法的 left 区间: [0, l_digit + 1)
            # 字母合法的 left 区间: [l_k_low, l_k_high)
            
            start = max(0, l_k_low)
            end = min(l_digit + 1, l_k_high)
            
            if start < end:
                ans += (end - start)

    print(ans)

if __name__ == "__main__":
    solve()