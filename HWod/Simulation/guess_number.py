def check(secret, guess):
    A = sum(secret[i] == guess[i] for i in range(4))  # 数字和位置都对的个数
    B = sum(min(secret.count(c), guess.count(c)) for c in set(secret)) - A  # B=sum(取交集数 - A)
    return A, B

n = int(input())
data = []

for _ in range(n):
    num, hint = input().split()
    data.append((num, int(hint[0]), int(hint[2])))  # 数字, A, B

ans = []

# 将猜测的数字和现在的数字一一对比, 且线索都一样, 即得到答案
for i in range(10000):
    s = str(i).zfill(4)  # 将整数 i 转为 4 位字符串，不足的用 '0' 在左侧填充
    if all(check(s, g)[0] == a and check(s, g)[1] == b for g, a, b in data):
        ans.append(s)

print(ans[0] if len(ans) == 1 else "NA")  # 答案有且只有一个