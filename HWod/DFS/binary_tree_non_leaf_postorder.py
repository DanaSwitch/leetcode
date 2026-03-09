import sys
sys.setrecursionlimit(10**6)

def solve():
    nums = list(map(int, sys.stdin.readline().split()))
    n = len(nums)  # 注意 n 是凑0前的长度
    nums = [0] + nums  # 改成下标1开始
    

    result = []  # 存储非叶子部分后序遍历

    def dfs(i):
        if i > n:
            return
        dfs(i * 2)
        dfs(i * 2 + 1)

        is_leaf = 2 * i > n and n > 1

        if not is_leaf:  # 碰到栈底回溯记录, 所以是后序遍历
            result.append(nums[i])
    
    dfs(1)
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    solve()