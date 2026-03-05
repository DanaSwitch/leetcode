s = input().replace(",", "").replace("111", "a").replace("11", "a").replace("1", "a")

ans = 0
for c in s:
    if c == 'a':
        ans += 1

print(ans)