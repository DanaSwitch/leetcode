"""
思想: 
差异值:不同才为1;  相似值:都为1才为1
统计最高位的位数:
位数相同 → 最高位位置相同(都是1)→ 该位进入 AND → AND 更大
位数不同 → 最高位位置不同 → 较长那个数的最高位只有它自己是1, 另一个是0 → 该位进入 XOR → XOR 更大
所以统计长度不同的组合数
"""
n = int(input())
arr = list(map(int, input().split()))

# 1 <= A[i] < 2^30, 最多30位
# 统计每个数字的二进制位数（即最高位位置），记录各位数出现的次数
bit_len_count = [0] * 31
for num in arr:
    # bin(num) 形如 '0b101'，减2去掉 '0b'
    bit_len_count[len(bin(num)[2:])] += 1  

# 统计最高位不同的二元组个数（即跨组的对数）
ans = 0
for i in range(31):
    for j in range(i + 1, 31):  # j > i 保证每对只数一次
        ans += bit_len_count[i] * bit_len_count[j]

print(ans)