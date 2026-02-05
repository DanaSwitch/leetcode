import sys
import collections

def solve():
    # 1. 高效读取输入
    s = sys.stdin.readline().strip()
    if not s:
        return

    n = len(s)
    target = n // 4
    
    # 2. 统计初始状态
    # count 记录的是【窗口以外】留在原地的字符数量
    count = collections.Counter(s)
    
    # 3. 特殊情况检查：如果一开始就都达标，不需要改
    if all(count[c] <= target for c in "WASD"):
        print(0)
        return

    min_len = n  # 记录最小替换长度
    left = 0     # 左指针
    
    # 4. 滑动窗口开始（右指针 right 主动移动）
    for right in range(n):
        # 【进窗】：s[right] 进入待替换区，所以“外面”的计数 -1
        count[s[right]] -= 1
        
        # 【检查】：只要“外面”剩下的所有字符都 <= target，说明多余的都在窗口里了
        # 此时窗口是合法的（可以通过修改窗口内的字来平衡整体）
        while all(count[c] <= target for c in "WASD"):
            # 记录当前合法窗口的长度，尝试更新最小值
            min_len = min(min_len, right - left + 1)
            
            # 【出窗】：尝试缩小窗口，看看 s[left] 能不能不替换
            # s[left] 移出待替换区，回到“外面”，计数 +1
            count[s[left]] += 1
            left += 1
            
    # 5. 输出最终结果
    print(min_len)

if __name__ == "__main__":
    solve()