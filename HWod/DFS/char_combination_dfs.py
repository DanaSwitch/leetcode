import sys

def solve():
    # 1. 处理输入
    line = sys.stdin.read().split()
    if len(line) < 2: return
    str, n_str = line[0], line[1]
    n = int(n_str)
    # 输入非法:
    for s in str:
        if s < 'a' or s > 'z':
            print(0)
            return
    
    # 2. 边界校验
    if n > len(str) or n <= 0:
        print(0)
        return
    
    # 3. 准备工作: 排序是剪枝的前提
    chars = sorted(list(str))
    used = [False] * len(chars)  #  used[i] = True 表示在纵向递归深入时正在使用char[i]
    
    def dfs(last_idx, level):  # 上一个字符的索引, 层级
        # 递归出口
        if level == n:
            return 1  # 向上一层报告有一个解
        
        count = 0
        for i in range(len(chars)):
            # 剪枝逻辑：
            # 1. 已使用的字符跳过
            # 2. 相同的字符不能相邻 (chars[i] == chars[last_idx])
            # 3. 树层去重：如果当前字符和前一个相同，且前一个没在使用，说明这个分支已经跑过了
            if used[i]:
                continue
            if last_idx != -1 and chars[i] == chars[last_idx]:
                continue
            # 已经排好序了, 相同的字母会挨在一起
            if i > 0 and chars[i] == chars[i-1] and not used[i-1]:
                continue
            
            used[i] = True
            count += dfs(i, level + 1) # 传递当前索引作为下一层的 last_idx
            used[i] = False # 回溯
            
        return count

    print(dfs(-1, 0))

if __name__ == "__main__":
    solve()