import sys
sys.setrecursionlimit(10**6)

def solve():
    n = int(input())
    
    memo = {}
    def dfs(i):
        # 出口
        if i < 3:
            return (0, 1)  # 拆分次数, 份数
        
        # 记忆化搜索
        if i in memo:
            return memo[i]
        
        # 分成两份
        a, b = (i+1)//2, i//2
        cut1, parts1 = dfs(a)
        cut2, parts2 = dfs(b)
        # 加1是因为 i 自身要切一刀
        result = (1 + cut1 + cut2, parts1 + parts2)

        memo[i] = result
        return result
    cut, parts =  dfs(n)
    print(cut, parts)

if __name__ == "__main__":
    solve()