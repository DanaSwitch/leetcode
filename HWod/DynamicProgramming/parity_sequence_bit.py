def solve():
    # 读取输入
    line = input().strip()
    if not line:
        return
    n = int(line)

    # dp_odd[i] 表示以数字 i 开头的所有“全奇数”数列的个数
    dp_odd = [0] * (n + 1)
    # dp_even[i] 表示以数字 i 开头的所有“全偶数”数列的个数
    dp_even = [0] * (n + 1)
    # dp_alt[i] 表示以数字 i 开头的所有“奇偶相间”数列的个数
    dp_alt = [0] * (n + 1)

    # 我们从 1 开始从小到大计算，因为大数字的结果依赖于小数字
    for i in range(1, n + 1):
        # 每一个数字本身都可以作为一个长度为 1 的数列
        # 比如 [1], [2], [3]...
        dp_odd[i] = 1 if i % 2 != 0 else 0
        dp_even[i] = 1 if i % 2 == 0 else 0
        dp_alt[i] = 1 # 任何数开头都可以开始奇偶相间
        
        limit = i // 2 # 下一个数不能超过当前数的一半
        
        for j in range(1, limit + 1):
            if i % 2 != 0: # 如果当前数 i 是奇数
                # 1. 全奇数：只能接在之前算好的奇数开头数列前面
                dp_odd[i] += dp_odd[j]
                # 2. 奇偶相间：奇数后面必须接偶数开头的“相间”数列
                if j % 2 == 0:
                    dp_alt[i] += dp_alt[j]
            
            else: # 如果当前数 i 是偶数
                # 1. 全偶数：只能接在之前算好的偶数开头数列前面
                dp_even[i] += dp_even[j]
                # 2. 奇偶相间：偶数后面必须接奇数开头的“相间”数列
                if j % 2 != 0:
                    dp_alt[i] += dp_alt[j]

    # 最后的结果：
    # 注意：单元素数列 [n] 在三个 dp 数组里都被算了一次。
    # 题目要求是“全奇 OR 全偶 OR 相间”，我们需要把它们加起来。
    # 但要减去重复算的 [n] 两次。
    
    if n % 2 != 0:
        # n 是奇数时：结果 = 全奇数开头的 + 相间开头的 - 1 (重复的[n])
        # 因为奇数不能开头“全偶”数列
        print(dp_odd[n] + dp_alt[n] - 1)
    else:
        # n 是偶数时：结果 = 全偶数开头的 + 相间开头的 - 1 (重复的[n])
        print(dp_even[n] + dp_alt[n] - 1)

if __name__ == "__main__":
    solve()