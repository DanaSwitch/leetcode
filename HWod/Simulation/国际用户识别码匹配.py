# 匹配函数
def judge(pattern, s):
    if pattern == '*':
        return True
    n, m = len(s), len(pattern)
    i = 0
    while i < n and i < m:
        if pattern[i] == s[i]:
            pass
        elif pattern[i] == '?':
            # 偶数位置不能匹配又不相同
            if i % 2 == 0:
                return False
        elif pattern[i] == '*':
            # pattern末尾为*
            if i == m - 1:
                return True
            # 后缀匹配    
            suffix = pattern[i + 1:]
            pos = len(suffix) - 1
            j = n - 1
            while j >= i and pos >= 0:
                if suffix[pos] == s[j]:
                    pass
                elif suffix[pos] == '?':
                    if j % 2 == 0:
                        break
                else:
                    break
                j -= 1
                pos -= 1
            return pos < 0
        else:
            return False
        i += 1
    # 从这里返回说明前15格字符不存在* 所以必需两者长度相同/ 或者pattern.size 长度比str大一,并且最后一个为*
    return m == n or (m == n + 1 and pattern[m-1] == '*')

settings = input().split(',')
number = input()
res = []

for pattern in settings:
    if judge(pattern, number):
        res.append(pattern)

if not res:
    print("null")
else:
    print(",".join(sorted(res)))
